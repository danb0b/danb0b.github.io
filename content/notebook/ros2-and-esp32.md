---
title: Running Ros2 on an ESP32
tags: 
- virtualbox
- ROS2
- esp32
summary: ""
---

## Virtualbox guest master setup


1. create a virtual machine
    1. Networking: Select bridged networking
1. install ubuntu 22.04 server edition
1. update and upgrade
1. [remove firefox and snapd](/notebook/removing-firefox-snap/)
1. install helpful tools

    ```bash
    sudo apt install -y net-tools
    ```

1. install ubuntu-desktop-minimal

    ```bash
    sudo apt install -y ubuntu-desktop-minimal
    ```

1. install vm guest additions prerequisites

    ```bash
    sudo apt install -y gcc make perl
    ```

1. install vm guest additions
    1. go to virtualbox  menu and select "install guest additions"
    1. navigate to the cdrom and run autorun.sh
1. restart


1. Install ROS2

    ```bash
    sudo apt install -y software-properties-common
    sudo add-apt-repository universe
    sudo apt update && sudo apt install -y curl
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
    sudo apt update && sudo apt upgrade -y
    sudo apt install -y ros-humble-desktop ros-dev-tools
    ```

1. install cyclone-dds

    ```bash
    sudo apt install -y ros-humble-rmw-cyclonedds-cpp
    ```

1. add configuration info to .bashrc:

    ```bash
    echo "source /opt/ros/humble/setup.bash" >> .bashrc
    echo "RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> .bashrc
    ```

1. install ros-bridge server

    ```bash
    sudo apt install -y ros-humble-rosbridge-server 
    ```

1. launch rosbridge

    ```bash
    ros2 launch rosbridge_server rosbridge_websocket_launch.xml 
    ```

1. Publish something using rosbridge
1. echo it in ROS

    ```bash
    ros2 topic list 
    ros2 topic echo /hadabot/log/info 
    ```

## External resources

* <https://medium.com/@hadabot/use-ros2-an-esp32-running-micropython-and-the-web-browser-to-control-a-motor-driver-a88f9b1e7489>