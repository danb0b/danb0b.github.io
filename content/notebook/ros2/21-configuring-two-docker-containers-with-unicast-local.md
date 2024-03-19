---
title: Demonstrating Unicast in ROS2 on two docker containers with CycloneDDS
weight: 21
tags:
- docker
- linux
- ubuntu
- ros2
- cyclonedds
- unicast
---

## Introduction

In other articles I have shown how to configure a virtual machine to talk over cycloneDDS using unicast rather than the default multicast.  This article details the steps required to do the same in docker.  Docker is much lighter weight to set up than a virtual machine, and is a useful choice if you want to test your network.

Key points of this article:

* How to assign a unique ip address to a docker container that is visible on your physical network, making it usable for ROS communication with non-docker devices.
* How to configure unicast, specifically cyclonedds, to work with a docker container, to avoid multicast issues on your local network.
* How to embed this logic in a self-contained, multi-container application using docker compose.

## File Structure

make a new folder with the following subfolders and (empty) files.

```
.
├── build
│   └── Dockerfile
├── docker-compose.yml
├── listener-shared
│   └── cyclonedds_pc.xml
└── talker-shared
    └── cyclonedds_pc.xml
```

## Dockerfile

This dockerfile starts with the ros humble image, sets some environment variables, and installs cyclonedds, amongst some other helpful utilities.

```dockerfile
FROM osrf/ros:humble-desktop
# WORKDIR /temp
    
ENV ROS_DOMAIN_ID=0
ENV ROS_LOCALHOST_ONLY=0
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ENV CYCLONEDDS_URI=/root/shared/cyclonedds_pc.xml

RUN apt update && \ 
    apt install -y \ 
    iputils-ping \ 
    software-properties-common \
    ros-humble-rmw-cyclonedds-cpp \ 
    ros-dev-tools
```

## Docker Compose

This example makes use of the ipvlan driver to allow each docker container to obtain an ip address on the local network.

> This example assumes a local subnet of ```192.168.8.1/24```.  You will need to modify this to suit your own local settings.

```yaml
version: '2'

services:
  ros1:
    container_name: ros2-talker
    build: ./build
    hostname: ros-host2
    domainname: test
    networks:
      network:
        ipv4_address: 192.168.8.50
    volumes:
      - ./talker-shared:/root/shared
    command: bash -c "source /opt/ros/humble/setup.bash && ros2 run demo_nodes_cpp talker"
    restart: unless-stopped
  ros2:
    container_name: ros2-listener
    build: ./build
    hostname: ros-host
    domainname: test
    networks:
      network:
        ipv4_address: 192.168.8.51
    volumes:
      - ./listener-shared:/root/shared
    command: bash -c "source /opt/ros/humble/setup.bash && ros2 run demo_nodes_cpp listener"
    restart: unless-stopped

networks:
  network:
    driver: ipvlan
    driver_opts:
      parent: wlp1s0
      ipvlan-mode: l2
    ipam:
      driver: default
      config:
        - subnet: 192.168.8.0/24
          gateway: 192.168.8.1
          ip_range: 192.168.8.1/24
```

## Config file

make two subfolders "./talker-shared" and ```./listener-shared```.  Create a file in each called ```cyclonedds_pc.xml```. Paste in the following:

This assumes you have two docker containers with ip addresses 192.168.98.50 (and 51), as well as another local pc with address 192.168.8.120 on the network you would like to connect together.

```xml
<CycloneDDS>
    <Domain>
        <General>
            <DontRoute>true</DontRoute>
            <AllowMulticast>false</AllowMulticast>
            <EnableMulticastLoopback>true</EnableMulticastLoopback>
        </General>
        <Discovery>
          <ParticipantIndex>auto</ParticipantIndex>
          <Peers>
            <Peer Address="192.168.8.120"/>
            <Peer Address="192.168.8.50"/>
            <Peer Address="192.168.8.51"/>
          </Peers>
    </Discovery>
    </Domain>
</CycloneDDS>
```


## Building

This command uses the build capabilities of docker compose the first time.  If you change anything in the dockerfile and want to rebuild, you can use the command.

```
docker compose up --force-recreate --build
```

Despite all flags, if docker sees a locally cached layer, it will not rebuild or re-acquire it.  This means you may also need to use:

```
docker build --no-cache -t <image-name> /path/to/dockerfile
```

if you want to docker to rebuild without any cached layers (for example if the build command hasn't changed but the online repo has been updated.)

## Testing

Finally, run```docker compose up``` to run the containers in the foreground.  To kill the containers you can use ```ctrl+c```. You can alternately run them in the background using ```docker compose up -d```.

You can now observe the functional docker containers sending messages over the network.  Using a separate machine or VM, run 

```ros2 run demo_nodes_cpp listener```

## Shutting down

To take down the containers and associated networks, enter ```docker compose down```.