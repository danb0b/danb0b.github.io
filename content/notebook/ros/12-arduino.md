---
---

## Introduction

These instructions were for how to create the package from scratch.  if you are using the idealab_ros repository you will not have to do all the steps

## Instructions

1. add the arduino to the usb filter list in virtualbox on the host machine
1. plug in usb device and find out device info, including port

    ```bash
    dmesg
    #dmesg | grep arduino
    ```

1. boot ubuntu, open terminal (ctrl+t) navigate to /dev, and list devices 

    ```bash
    cd /dev
    ls -la
    ```

1. install arduino

    ```bash
    sudo apt update
    sudo apt install -y arduino
    ```

1. clone hx711 library

    ```bash
    git clone https://github.com/idealabasu/HX711.git
    ```

1. open arduino
1. install hx711 library
1. select port (/ttyACM0)
1. select programmer (AVRisp mkII)
1. make new directory in src/

    ```bash
    catkin_create_pkg force_plate std_msgs rospy roscpp
    ```
    
1. edit package as before
    1. add message
    1. catkin_make
    1. commit git

1. make scripts

    ```bash
    roscd force_plate/
    mkdir scripts
    cd scripts
    # pull talker
    wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py
    chmod +x talker.py 
    #wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py
    #chmod +x listener.py
    ```
    
1. Modify as needed