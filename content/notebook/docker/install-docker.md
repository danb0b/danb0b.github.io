---
title: Install Docker
tags:
  - docker
  - linux
weight: 10
summary: " "
---

From [here](https://docs.docker.com/engine/install/ubuntu/)

1. Install and test

    ```bash
    sudo apt remove docker docker.io containerd runc
    sudo apt remove docker*

    sudo apt install -y ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    sudo apt update
    sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    
    sudo service docker start
    sudo docker run hello-world
    ```

1. Add current user to docker group

    ```bash
    sudo usermod -a -G docker $USER
    ```

1. Login:

    ```bash
    docker login -u <username>
    ```

1. Restart or logout/login

## Usage

```bash
docker pull alpine
docker run -it alpine /bin/sh
docker run -v /home/<username>/<path>/:/test -it alpine sh

docker pull ubuntu
docker run -it ubuntu bash
```

##

```bash
docker container ls -a
docker container rm <id>

docker image ls -a
docker image rm <id>
docker image rm -f <id>

docker login
docker commit <user/repo>
docker push <user/repo>
docker history --no-trunc <user/repo>
```

## Make a fresh docker image

```bash
mkdir docker
cd docker
nano Dockerfile
```
```dockerfile
FROM ubuntu:22.04
 
RUN apt update && apt install -y nginx 

LABEL maintainer="danb0b"
LABEL version="1.0"
LABEL description="A simple image running Nginx on Debain 10"
 
EXPOSE 80/tcp
 
CMD ["nginx","-g","daemon off;"]
```
```bash
docker build -t myapp:v1 .
docker run -p 80:80 myapp:v1
```