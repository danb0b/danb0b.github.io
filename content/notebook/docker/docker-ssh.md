---
title: using ssh inside docker
---

## Introduction

This article shows the following:

* How to create a custom user in a dockerfile
* how to setup ssh for easy login
* how to set up ssh for use with a physical network, even one through a wifi NIC (which has historically been harder)


## Folder structure

```
.
├── build
│   ├── Dockerfile
├── docker-compose.yaml
```

## Dockerfile

```dockerfile
FROM ubuntu:latest
WORKDIR /test
ENV MYUSER=danaukes
ENV MYGROUP=danaukes
ENV MYUID=1000
ENV MYGID=1000

RUN apt update && apt install -y openssh-server iputils-ping git sudo net-tools

RUN addgroup --gid ${MYGID} ${MYGROUP} && \
    useradd -p $(perl -e 'print crypt($ARGV[0], "password")' 'test') -u ${MYUID} -g ${MYGID} -G adm,sudo ${MYUSER} && \
    mkdir /home/${MYUSER} && \
    chown ${MYUSER}:${MYGROUP} /home/${MYUSER} && \
    echo "${MYUSER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/nopasswd

USER ${MYUSER}
```

## Docker compose

```yaml
version: "3.9"
services:
  web:
    build: ./build
    user: danaukes
    networks:
      ubuntu-network:
        ipv4_address: "192.168.4.99"
    dns:
      - 192.168.4.1
    ports:
      - 22/tcp
    command: bash -c "sudo service ssh start && sleep infinity"
    restart: unless-stopped

networks:
  ubuntu-network:
    driver: ipvlan
    driver_opts:
      parent: wlp1s0
      ipvlan-mode: l2
    ipam:
      driver: default
      config:
        - subnet: 192.168.4.0/24
          gateway: 192.168.4.1
          ip_range: 192.168.4.1/24

```


## Notes and snippets

may need to run this to enable the kind of networking needed above:

```bash
sysctl -w net.ipv4.ip_forward=1
sudo iptables -P FORWARD ACCEPT
 
sudo service docker restart
docker system prune
```

```bash
apt update
apt install -y openssh-server iputils-ping
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
#apt install nano
#nano /etc/ssh/sshd_config
service ssh start
#sudo passwd root
```

```bash
sudo /etc/init.d/ssh reload 
```

```bash
docker compose up --force-recreate --build ros -d
docker exec -it --user user1 d64dd7a05bb3 /bin/bash
```

```
echo "export PATH=/opt/ros/galactic/bin:\$PATH" >> ~/.bashrc
```

## External Resources

* <https://stackoverflow.com/questions/64142811/docker-container-has-access-to-internet-but-not-the-local-network>
* <https://lurps.rocks/posts/docker-compose-ipvlan/>
* <https://automaticaddison.com/how-to-install-and-launch-ros2-using-docker/>
* <https://devanshdhrafani.github.io/blog/2021/04/15/dockerros2.html>
* <https://docs.ros.org/en/galactic/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html>
* <https://serverfault.com/questions/958367/how-do-i-give-a-docker-container-its-own-routable-ip-on-the-original-network>
* <https://stackoverflow.com/questions/35742807/docker-1-10-containers-ip-in-lan>
* <https://www.reddit.com/r/docker/comments/jt032d/how_to_give_a_container_its_own_ip_address_on/>
* <https://docs.docker.com/network/bridge/>
* <https://docs.docker.com/network/macvlan/>
* <https://lurps.rocks/posts/docker-compose-ipvlan/>


* <https://stackoverflow.com/questions/39855304/how-to-add-user-with-dockerfile>
* <https://askubuntu.com/questions/668129/password-does-not-work-with-useradd-p>
* <https://stackoverflow.com/questions/30063907/docker-compose-how-to-execute-multiple-commands>
* <https://duckduckgo.com/?t=ffab&q=how+to+rebuild+docker+image+from+compose&ia=web>
* <https://docs.ros.org/en/galactic/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html>

> Note: Another important thing to remember (Macvlan and IPvlan): Traffic to and from the master device cannot be sent to and from slave devices. If you need to enable master to slave communication see section "Communication with the host (default-ns)" in the "IPVLAN – The beginning" paper published by one of the IPvlan authors (Mahesh Bandewar). found [here](https://stackoverflow.com/questions/35742807/docker-1-10-containers-ip-in-lan)