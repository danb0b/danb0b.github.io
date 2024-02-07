---
title: Setting up two ROS2 containers in Docker
tags:
- docker
- ros2
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
