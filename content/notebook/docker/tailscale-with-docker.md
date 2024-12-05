---
title: Using tailscale with docker
summary: " "
---

1. Settings-->keys
1. check reusable, ephemeral, pre-approved
1. Copy the key
1. paste the following in your bashrc

    ```bash
    export DOCKERKEY=<your-key-here>
    ```

1. paste the following to run docker so that you can access all other devices on tailnet.  In this case, replace <my_subnet> with your subnet, eg 10.0.0.0/24

    ```bash
    docker run -v /var/lib:/var/lib -v /dev/net/tun:/dev/net/tun --network=host --cap-add=NET_ADMIN --cap-add=NET_RAW --env TS_AUTHKEY=$DOCKERKEY_PERM --env TS_ROUTES=10.0.0.0/8 tailscale/tailscale
    ```

    ```bash
    docker run -v /var/lib:/var/lib -v /var/lib/tailscale:/var/lib/tailscale -d /dev/net/tun:/dev/net/tun --network=host --cap-add=NET_ADMIN --cap-add=NET_RAW --env TS_AUTHKEY=$DOCKERKEY_PERM --env TS_ROUTES=10.0.0.0/8 tailscale/tailscale
    ```

```bash
sudo docker run -d --name=tailscaled -v /var/lib:/var/lib -v /dev/net/tun:/dev/net/tun --network=host --cap-add=NET_ADMIN --restart unless-stopped --cap-add=NET_RAW --env TS_AUTHKEY=[AUTH KEY] --env TS_EXTRA_ARGS=--advertise-exit-node --env TS_ROUTES=[SUBNET] tailscale/tailscale
```

## Recipe 1: install tailscale in your desired ubuntu docker image

### Folder Structure

```txt
.
├── build
│   └── Dockerfile
├── docker-compose.yml
├── lib
│   └── tailscale
```

### Dockerfile

```dockerfile
FROM ubuntu:22.04

RUN apt update && apt install -y curl
RUN curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/focal.noarmor.gpg | tee /usr/share/keyrings/tailscale-archive-keyring.gpg >/dev/null && \
curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/focal.tailscale-keyring.list | tee /etc/apt/sources.list.d/tailscale.list && \
apt update && \
apt install -y tailscale

```

### Docker compose

```yaml
version: "3.9"
services:
  tailscaled:
    build: ./build
    volumes:
      - ./lib:/var/lib
      - /dev/net/tun:/dev/net/tun
    hostname: docker-ub
    environment:
      - TS_AUTHKEY=${DOCKERKEY_PERM}
    #   - TS_ROUTES=10.0.0.0/8
      - TS_USERSPACE=0
      - TS_STATE_DIR=/var/lib/tailscale
      - TS_HOSTNAME=docker1
    cap_add: 
      - NET_ADMIN
      - NET_RAW
    command: bash -c "tailscaled & tailscale up --authkey ${TS_AUTHKEY} && sleep infinity"
    restart: unless-stopped
```

## Recipe 2: as a "Sidecar"

```txt
.
├── docker-compose.yml
├── html
│   └── index.html
└── lib
    └── tailscale
```

Html

```html
Hello, I'm Dan, at  <a href='https://danaukes.com/'>danaukes.com</a>
```

docker compose

```yaml

version: "3.9"
services:
  tailscaled:
    image: tailscale/tailscale:latest
    # ports:
      # - 8080:80
    volumes:
      - ./lib:/var/lib
      - /dev/net/tun:/dev/net/tun
    environment:
      - TS_AUTHKEY=${DOCKERKEY_PERM}
      # - TS_ROUTES=172.0.0.0/8
      - TS_USERSPACE=0
      - TS_STATE_DIR=/var/lib/tailscale
      - TS_HOSTNAME=docker1
      # - TS_EXTRA_ARGS=--accept-routes
    cap_add: 
      - NET_ADMIN
      - NET_RAW

  test-service:
    image: nginx:latest
    network_mode: "service:tailscaled"

    volumes:
      - ./html:/usr/share/nginx/html
```

## Deprecated suggestions

sudo ip tuntap add dev tun0 mode tun
sudo ip addr add 10.0.0.1/24 dev tun0
sudo ip link set up dev tun0

## External Resources

* <https://hub.docker.com/r/tailscale/tailscale>
* <https://www.wundertech.net/how-to-set-up-tailscale-on-docker/>
* <https://tailscale.com/kb/1184/docker-desktop/>
* <https://tailscale.com/kb/1282/docker/>
* <https://tailscale.com/blog/kubecon-21/>

### TUN devices

* <https://www.baeldung.com/linux/tun-interface-purpose>
    * [OSI Model](https://www.baeldung.com/cs/osi-model)
* <https://stackoverflow.com/questions/59451531/how-to-create-tun-interface-inside-docker-container-image>
* <https://www.kernel.org/doc/html/latest/networking/tuntap.html>
* <https://stackoverflow.com/questions/17529345/ubuntu-remove-network-tap-interface>

### Docker Compose

* <https://docs.docker.com/compose/environment-variables/set-environment-variables/>
* <https://docs.docker.com/engine/reference/commandline/run/>
* <https://docs.docker.com/compose/compose-file/compose-file-v3/>

### Do it yourself

* <https://rnorth.org/tailscale-docker/>
* <https://www.reddit.com/r/Tailscale/comments/w8gda3/official_docker_image_with_subnet_routing/>
* <https://hub.docker.com/r/fastandfearless/tailscale/dockerfile>
* <https://forum.level1techs.com/t/truenas-scale-ultimate-home-setup-incl-tailscale/186444/3>
* <https://pastebin.com/vC2vzyjG>
* <https://www.reddit.com/r/Tailscale/comments/103ib0a/tailscale_on_portainer_via_stack/>
* jonohill
    * <https://github.com/hillnz/docker-tailscale>
    * <https://hub.docker.com/r/jonoh/tailscale>

### Sidecar

* <https://asselin.engineer/tailscale-docker>

### nginx

* <https://awstip.com/creating-a-simple-web-server-with-docker-a-step-by-step-guide-to-running-your-web-server-as-a-2992ce2051e3>
