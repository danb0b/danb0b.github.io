---
title: caddy set up
tags:
- caddy
- tailscale
- docker
---


## Domain

1. go to domain management -> advanced DNS
1. add an ```A``` record pointing ```test``` (as an example) to the ip address of public server

## Public server

1. get ip address to supply to previous step
1. open up ports
1. create a new folder for a docker container

## Tailscale Admin Panel

We are assuming you have manual "device approval" turned off on your tailnet: <https://tailscale.com/kb/1099/device-approval>

1. Create a new "auth key" here: <https://login.tailscale.com/admin/settings/keys>
    * set to "ephemeral"
    * set "reusable"
1. Copy the private key

## public server docker setup

First add the tailscale private key to your environment variables

```bash
echo 'export DOCKERKEY_AWS="<key you copied>"' >> ~/.bashrc
source ~/.bashrc
```


file structure:

```bash
.
├── Dockerfile
├── build.sh
├── conf
│   └── Caddyfile
├── docker-compose.yaml
```

Dockerfile

```bash
FROM caddy:2-alpine
RUN apk add --no-cache \
    tailscale \
    bash
```

build.sh

```bash
#!/usr/bin/sh
docker build -t my_caddy ./
```

docker-compose.yaml

```yaml
services:
  caddy_aws:
    hostname: caddy
    container_name: caddy
    image: my_caddy
    cap_add:
      - NET_ADMIN
      - NET_RAW
    ports:
      - 80:80
      - 5555:5555
    volumes:
      - ./conf:/etc/caddy
      - ./site:/srv
      - ./data:/data
      - ./config:/config
      - ./varlib-tailscale:/var/lib/tailscale
      - /dev/net/tun:/dev/net/tun
    environment:
      - DOCKERKEY_AWS
      - TS_USERSPACE=0
      - TS_STATE_DIR=/var/lib/tailscale
      - TS_HOSTNAME=caddy_aws
    restart: unless-stopped
    command: bash -c "tailscaled & tailscale up --authkey '${DOCKERKEY_AWS}' &&  caddy run -c /etc/caddy/Caddyfile"
```

conf/Caddyfile

```conf
test.<domain-name>.com:80 {
    reverse_proxy {
        to <tailscale-hostname>:80
    }
}

http://test.<domain-name>.com:5555 {
    reverse_proxy {
        to <tailscale-hostname>:5555
    }
}
```


## Internal Server (tailscale-hostname)

In this example we are assuming the server itself is on tailscale already

create a new directory for your internal docker server.  This can be anything.  We are just going to create a simple caddy server here.

```
.
├── conf
│   └── Caddyfile
├── docker-compose.yaml
```

docker-compose.yaml

```yaml
services:
  caddy:
    image: "caddy:2-alpine"
    cap_add:
      - NET_ADMIN
    ports:
      - 80:80
      - 5555:5555
    volumes:
      - ./conf:/etc/caddy
      - ./site:/srv
      - ./data:/data
      - ./config:/config
    restart: unless-stopped
```

conf/Caddyfile

```conf
:80 {
        respond "Hello from my network"
}
:5555 {
        respond "Hello from port 5555 of my network"
}
```


## external resources

* <https://yashgarg.dev/posts/reverse-proxy-cgnat/>
* <https://tailscale.com/kb/1099/device-approval>
* <https://hub.docker.com/_/caddy/>