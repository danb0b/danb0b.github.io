---
title: Install Docker
tags:
  - docker
  - linux
---

From [here](https://docs.docker.com/engine/install/ubuntu/)

1. Install and test

    ```bash
    sudo apt remove docker docker.io containerd runc
    sudo apt remove docker*
    sudo apt update
    sudo apt install ca-certificates curl gnupg lsb-release
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt update
    sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    sudo apt install docker-compose
    sudo docker run hello-world
    ```

1. Add current user to docker group

    ```bash
    sudo usermod -a -G docker $USER
    ```

1. Restart

## USE

```bash
docker pull alpine
docker run -it alpine /bin/sh
docker run -v /home/<username>/<path>/:/test -it alpine sh

docker pull ubuntu
docker run -it ubuntu bash
```