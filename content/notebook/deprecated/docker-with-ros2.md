---
title: getting docker networking working with ros2
tags:
- docker
- ros
- ros2
- linux
summary: " "
---


## Deprecated

This tutorial is deprecated because

it uses ipvlan instead of macvlan, making it not useful for wifi nics
it's about installing docker inside two vms... I have better examples now.

## Virtualbox guest master setup

- Networking
    - Select Internal networking

        according to [here](https://www.virtualbox.org/manual/ch06.html#network_internal), internal networking fully supports broadcast.  I suspect bridged will too...

1. create a virtual machine
1. install ubuntu 22.04 server edition
1. update
1. [remove firefox and snapd](/notebook/removing-firefox-snap/)
1. install helpful tools

    ```bash
    sudo apt install -y net-tools
    ```

1. install ubuntu-desktop-minimal

    ```bash
    sudo apt install -y ubuntu-desktop-minimal
    ```

1. [install docker](/notebook/docker/install-docker/), ensuring to add docker group to your user.
1. install vm guest additions prerequisites

    ```bash
    sudo apt install -y gcc make perl
    ```

1. install vm guest additions
    1. go to virtualbox  menu and select "install guest additions"
    1. navigate to the cdrom and run autorun.sh
1. restart
1. pull your desired ros2 image. For example:

    ```bash
    docker pull osrf/ros:galactic-desktop
    ```

1. shutdown the guest
1. save a snapshot
1. create two linked clones, regenerating all network interface ids and MACs.

## Internal Networking

### Guest 1 Setup

#### configuration

select "internal network"

#### netplan

```bash
sudo cp /etc/netplan/00-installer-config.yaml /etc/netplan/00-installer-config.yaml.bak
cat << EOT sudo tee /etc/netplan/00-installer-config.yaml 
network:
  ethernets:
    enp0s3:
      addresses:
      - 192.168.0.120/24
      dhcp4: no
      dhcp6: no
  version: 2
EOT
```

#### docker-compose

```bash
mkdir ~/docker
cd ~/docker
cat << EOT >docker-compose.yml
version: '2'

services:
  ros:
    container_name: ros2
    image: osrf/ros:galactic-desktop
    hostname: ros-host
    domainname: test
    networks:
      network:
        ipv4_address: 192.168.0.121
    command: ros2 run demo_nodes_cpp talker
    restart: unless-stopped

networks:
  network:
    driver: ipvlan
    driver_opts:
      parent: enp0s3
      ipvlan-mode: l2
    ipam:
      driver: default
      config:
        - subnet: 192.168.0.0/24
          gateway: 192.168.0.1
          ip_range: 192.168.0.1/24
EOT
```

### Guest 2

#### configuration

select "internal network"

#### netplan

```bash
sudo cp /etc/netplan/00-installer-config.yaml /etc/netplan/00-installer-config.yaml.bak
cat << EOT sudo tee /etc/netplan/00-installer-config.yaml 
network:
  ethernets:
    enp0s3:
      addresses:
      - 192.168.0.130/24
      dhcp4: no
      dhcp6: no
  version: 2
EOT
```

#### docker-compose

```bash
mkdir ~/docker
cd ~/docker
cat << EOT >docker-compose.yml
version: '2'

services:
  ros:
    container_name: ros2
    image: osrf/ros:galactic-desktop
    hostname: ros-host
    domainname: test
    networks:
      network:
        ipv4_address: 192.168.0.131
    command: ros2 run demo_nodes_cpp listener
    restart: unless-stopped

networks:
  network:
    driver: ipvlan
    driver_opts:
      parent: enp0s3
      ipvlan-mode: l2
    ipam:
      driver: default
      config:
        - subnet: 192.168.0.0/24
          gateway: 192.168.0.1
          ip_range: 192.168.0.1/24
EOT
```

### Run

in clone 1 and 2, navigate to ~/docker and type

```bash
docker compose up
```

when done, please ensure you  clean up your network interfaces on each guest clone by typing

```bash
docker compose down
```

## Bridged Networking with a physical router

This example assumes a subnet of 192.168.8.xxx from the router.  Go to both guests and select bridged networking.  The guests ip addresses themselves can be assigned by the router's dhcp server in this example.

### clone 1 netplan

```bash
cat << EOT sudo tee /etc/netplan/00-installer-config.yaml 
network:
  ethernets:
    enp0s3:
#      addresses:
#      - 192.168.8.10/24
      dhcp4: yes
      dhcp6: no
  version: 2
EOT
```

### clone 1 docker-compose.yml

```bash
cat << EOT >~/docker/docker-compose.yml
version: '2'

services:
  ros:
    container_name: ros2
    image: osrf/ros:galactic-desktop
    hostname: ros-host
    domainname: test
    networks:
      network:
        ipv4_address: 192.168.8.11
    command: ros2 run demo_nodes_cpp talker
    restart: unless-stopped

networks:
  network:
    driver: ipvlan
    driver_opts:
      parent: enp0s3
      ipvlan-mode: l2
    ipam:
      driver: default
      config:
        - subnet: 192.168.8.0/24
          gateway: 192.168.8.1
          ip_range: 192.168.8.1/24
EOT
```

### clone 2 netplan

```bash
cat << EOT sudo tee /etc/netplan/00-installer-config.yaml 
# This is the network config written by 'subiquity'
network:
  ethernets:
    enp0s3:
#      addresses:
#      - 192.168.8.20/24
      dhcp4: yes
      dhcp6: no
  version: 2
EOT
```

### clone 1 docker-compose.yml

```bash
cat << EOT >~/docker/docker-compose.yml
version: '2'

services:
  ros:
    container_name: ros2
    image: osrf/ros:galactic-desktop
    hostname: ros-host
    domainname: test
    networks:
      network:
        ipv4_address: 192.168.8.21
    command: ros2 run demo_nodes_cpp listener
    restart: unless-stopped

networks:
  network:
    driver: ipvlan
    driver_opts:
      parent: enp0s3
      ipvlan-mode: l2
    ipam:
      driver: default
      config:
        - subnet: 192.168.8.0/24
          gateway: 192.168.8.1
          ip_range: 192.168.8.1/24
EOT
```
