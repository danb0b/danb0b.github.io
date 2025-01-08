---
title: Creating a custom Photon Package
weight: 150
tags:
- ros
- ubuntu
- linux
summary: " "
---
## Introduction

These instructions were used to create the photon package.  Please see the package in the src directory to see the resulting code and setup

## Instructions

1. Create package

    ```bash
    cd code_idealab_ros/src
    catkin_create_pkg photon_tcp std_msgs rospy roscpp
    ```

1. Create message

    ```bash
    roscd photon_tcp/
    mkdir msg
    nano data.msg
    ```

1. paste in:

    ```bash
    string ip_address
    string data
    ```

1. follow instructions for adding a messsage
1. follow instructions for adding a script
1. Modify script to suit needs
1. Make project

    ```bash
    roscd thorlabs_linear_actuator/
    catkin_make
    ```
