---
---


## ROS Instalation Summary

This is derived from [the official tutorial](https://wiki.ros.org/melodic/Installation/Ubuntu)

1. Run this code:  
 
    **Note:** We're using ```ros-melodic-desktop-full```

    ```bash
    #Setup your computer to accept software from packages.ros.org.
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

    #Set up your keys
    sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

    sudo apt update
    sudo apt install ros-melodic-desktop-full
    #sudo apt install ros-melodic-desktop
    #sudo apt install ros-melodic-ros-base

    #To find available packages, use:
    #apt search ros-melodic

    #It's convenient if the ROS environment variables are automatically added to your bash session every time a new shell is launched:
    echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
    echo "export EDITOR='nano -w'" >> ~/.bashrc #from https://wiki.ros.org/ROS/Tutorials/UsingRosEd
    source ~/.bashrc


    #To install tools and other dependencies for building ROS packages, run:
    sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
    #not sure if you need to do the next line.
    sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
    #sudo apt install python-rosdep

    sudo rosdep init
    rosdep update
    ```
1. Install catkin tools

    ```
    sudo apt install -y catkin-tools
    sudo apt install -y python3-pip python3-yaml
    sudo pip3 install rospkg catkin_pkg empy
    
    ```

1. Take a Snapshot

