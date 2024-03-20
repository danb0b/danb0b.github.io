---
title: Setting up Rosbridge in Ubuntu
tags:
- docker
- ros2
- rosbridge
weight: 40
---

## Introduction

Rosbridge is useful for connecting non-ROS systems to ROS.  Matlab, microcontrollers, and other systems often do not have an easy path for installing a full installation of ROS, but have ros-bridge clients that work with Rosbridge.  This article shows the following:

* how to get rosbridge working in Ubuntu
* how to start up ros bridge

This will run a program that listens on port 9090 and allows external devices to establish a websocket connection, and allowing messages to be passed in and out.

This assumes a working ROS installation.

## Steps

Set this in .bashrc:

RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

Install these

```bash
sudo apt update
sudo apt install -y iputils-ping software-properties-common ros-humble-rmw-cyclonedds-cpp ros-dev-tools ros-humble-rosbridge-server
```

## Run it

```bash
ros2 launch rosbridge_server rosbridge_websocket_launch.xml
```

