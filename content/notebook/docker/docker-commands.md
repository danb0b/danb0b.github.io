---
title: Common Docker Commands
weight: 20
tags:
  - docker
  - ubuntu
  - bash
  - cmd
summary: " "
---

# General Commands

```bash
docker images
docker pull
docker create
docker ps
docker attach 3378689f2069
```

## Deleting, cleanup

```bash
docker run —rm image_name
docker system prune
docker container prune
docker network prune
docker image prune
```

## Ubuntu Image

```bash
docker pull ubuntu
docker run -d -t ubuntu # run detached
docker run -it ubuntu /bin/bash
docker exec -it <containername> /bin/bash
apt update
docker compose run -it web /bin/bash
```

## Anaconda Image

```bash
docker pull continuumio/anaconda3
docker run -it continuumio/anaconda3 /bin/bash
```

## Set up gui:

[*https://dev.to/darksmile92/run-gui-app-in-linux-docker-container-on-windows-host-4kde*]

## ROS Stuff:

Modified from:[*https://jack-kawell.com/2019/09/11/setting-up-ros-in-windows-through-docker/*]


### To download and install and run ros:

```bash
docker pull osrf/ros:melodic-desktop-full
docker run \--name ros-dev -it osrf/ros:melodic-desktop-full bash
echo source \"/opt/ros/melodic/setup.bash\" \>\> \~/.bashrc
source \~/.bashrc
roscore
```

Anytime you want to develop in ROS, simply open a Powershell window and run the command below (make sure to substitute in the container name you chose to use before:

```bash
docker exec -it ros-dev bash
```

```bash
rqt_console
```

## Setup vcXsrv

Put in your wifi's ip address:

```bash
echo \'export DISPLAY=192.168.0.21:0.0\' \>\> \~/.bashrc
echo \'export DISPLAY=10.153.3.125:0.0\' \>\> \~/.bashrc
```

## To install a terminal-compatible text editor

```bash
apt update
apt install -y nano
```

## Accessing usb devices (not working):

[*https://stackoverflow.com/questions/24225647/docker-a-way-to-give-access-to-a-host-usb-or-serial-device*]

```bash
docker run \--name ros-dev -t -i \--privileged -v /dev:/dev osrf/ros:melodic-desktop-full bash
docker run \--name ros-dev -t -i \--privileged -v /dev/bus/usb:/dev/bus/usb osrf/ros:melodic-desktop-full bash
docker run -t -i \--privileged -v /dev:/dev ubuntu bash
```

## Jekyll

```bash
docker pull jekyll/builder
docker run \--name myjekyll -v c:/users/danaukes/websites:/srv/jekyll -it jekyll/builder bash
```




## SEe the dockerfile

from [here](https://stackoverflow.com/questions/77057173/how-to-download-dockerfile-from-docker-hub)

You cannot see the Dockerfile from Docker Hub, unless the maintainer add it. Many Docker hub repos add the GitHub link to point the Dockerfile but this is up to the maintaner.

What you can do to see the dockerfile is:

    pull the Docker image with docker pull <image-name>
    docker history <image-name>

From the docker history command, the first line indicates the parent docker image and in the following lines you can see all the steps used to compose the final image.

```bash
docker history --no-trunc <imagename>
```

## Build Options
### force rebuild

```bash
docker build --no-cache
```

### see all text

```bash
docker build --progress plain
```



  [*https://dev.to/darksmile92/run-gui-app-in-linux-docker-container-on-windows-host-4kde*]: https://dev.to/darksmile92/run-gui-app-in-linux-docker-container-on-windows-host-4kde
  [*https://jack-kawell.com/2019/09/11/setting-up-ros-in-windows-through-docker/*]: https://jack-kawell.com/2019/09/11/setting-up-ros-in-windows-through-docker/
  [*https://stackoverflow.com/questions/24225647/docker-a-way-to-give-access-to-a-host-usb-or-serial-device*]: https://stackoverflow.com/questions/24225647/docker-a-way-to-give-access-to-a-host-usb-or-serial-device

