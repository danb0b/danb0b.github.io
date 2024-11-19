---
title: Setting up two ROS2 containers in Docker
tags:
- docker
- ros2
summary: ""
---

## Introduction

Simple example of docker containers running ros over the physical network.

```yaml
version: '2'

services:
  ros1:
    container_name: ros2-talker
    image: osrf/ros:humble-desktop
    hostname: ros-host2
    domainname: test
    networks:
      network:
        ipv4_address: 192.168.8.11
    command: ros2 run demo_nodes_cpp talker
    restart: unless-stopped
  ros2:
    container_name: ros2-listener
    image: osrf/ros:humble-desktop
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
      parent: wlp1s0
      ipvlan-mode: l2
    ipam:
      driver: default
      config:
        - subnet: 192.168.8.0/24
          gateway: 192.168.8.1
          ip_range: 192.168.8.1/24

```



## External Resources

* <https://hub.docker.com/u/linuxserver>
* [docker-Tutorials-Docker - ROS Wiki](https://wiki.ros.org/docker/Tutorials/Docker)
* [How to use Docker (with ROS) · alecGraves-wiki Wiki](https://github.com/alecGraves/wiki/wiki/How-to-use-Docker-(with-ROS))
* [hub.docker.com](https://hub.docker.com/_/ros/)
* [jbohren-rosdocked- Tools for running ROS in docker with a shared username, home, and X11](https://github.com/jbohren/rosdocked)
* [Running 2 nodes in a single docker container [community-contributed]](https://index.ros.org/doc/ros2/Tutorials/Run-2-nodes-in-a-single-docker-container/)
* [Setting up ROS in Windows through Docker – Jack Kawell](https://jack-kawell.com/2019/09/11/setting-up-ros-in-windows-through-docker/)
* [Setting up ROS in Windows through WSL – Jack Kawell](https://jack-kawell.com/2019/06/24/ros-wsl1/)
* [Using ROS from a Docker image - Effective Robotics Programming with ROS - Third Edition](https://subscription.packtpub.com/book/hardware_and_creative/9781786463654/1/ch01lvl1sec11/using-ros-from-a-docker-image)
* <https://docs.ros.org/en/galactic/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html>
* <https://devanshdhrafani.github.io/blog/2021/04/15/dockerros2.html>

