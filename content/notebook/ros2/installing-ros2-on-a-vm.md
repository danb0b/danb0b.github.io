---
title: Installing ROS2 Humble on a Virtualbox VM
date: 2023-09-17
tags:
- virtualbox
- linux
- ubuntu
- ros2
---

## Introduction

How do you get a ROS2 system up and running on a virtual machine, and participating on your local network as if it were a real pc?  This tutorial helps you set up two virtual machine clones that can talk to each other without any special hardware other than your own pc, but look to any other device on the ROS network as if they are two full-fledged computers

This tutorial does not delve into ROS2 networking setup, but rather focuses on the plain install.  For more information on setting up ROS2 to work without multicast or over a vpn, please see the following articles:

* [Configuring ROS2 to work using UDP Unicast on a local network](/notebook/ros2/configuring-unicast-dds-with-cyclone/) 
* [Configuring ROS2 to work over a Tailscale VPN](/notebook/ros2/configuring-ros-over-tailscale/) 

## Prerequisites

> Ubuntu is one of the Linux distributions supported by ROS2 out of the box, with a repository and pre-compiled binaries.  For this tutorial, we assume you have already installed Ubuntu 22.04 LTS (Server Edition, 64 bit) on a virtual machine.  

<p>

> **Why Ubuntu Server?** I recommend Ubuntu server edition because there are some tools used by the server edition that are different in the desktop edition.  Installing the server edition and _then_ installing ```ubuntu-desktop-minimal``` will more closely mimic the installation on a desktop-less server than a full-fledged desktop install from the beginning.

Suggested machine parameters and install steps:

* Memory: Assign somewhere between 4096 and 8192 Mb of memory
* Hard Disk settings:
    * Use a .vdi
    * select "dynamically allocated
    * select at least 50Gb (100Gb recommended if possible)
* In the system --> processor tab, select 2-4 cpus if possible, keeping the slider out of the red region.
* Networking: use "Bridged Networking" with your wifi module selected (if possible).

    > **Note:** Bridged networking mode is extremely important for ROS2 to see this virtual machine and to be able to communicate with it.

* Ubuntu Installation:
    * Put in a unique machine name ("your server's name") that includes your name or initials
    * Deselect Docker from the optional services
* install virtual machine additions prerequisites using 

    ```bash
    sudo apt install gcc make perl build-essential
    ```
* then install virtual machine additions from the virtualbox menu.  with your desktop installed and your virtual machine running, 
    1. go to "devices" --> "install Guest Additions CD image"
    2. select yes to autorun
* consider 
    * [removing snap support](/notebook/removing-firefox-snap.md).  You will not need it and it can hang indefinitely in poor internet conditions
    * disabling automatic updates:

        ```bash
        sudo apt remove unattended-upgrades
        ```

        if you get a message like:

        ```bash
        Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 2131 (uWaiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 2131 (unattended-upgr)   
        ```

        ```bash
        sudo killall unattended-upgr
        ```


Finally first update and upgrade your apt installation, power down the machine and save a snapshot.

```bash
sudo apt update && sudo apt upgrade -y
```

## Instructions

Starting from a blank ubuntu server 22.04 vm, check for updates (if the vm has been off for a while, especially) and install the minimal ubuntu-desktop metapackage

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install ubuntu-desktop-minimal 
```

I also went through the work of removing the firefox snap and its dependencies, using [this post](/notebook/removing-firefox-snap/)

I noted my machine's ip address

```bash
ip a
```

I did another full upgrade

```bash
sudo apt update && sudo apt upgrade -y
```

I then installed ros2, using the instructions from [here](https://docs.ros.org/en/humble/Installation.html)

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL <https://raw.githubusercontent.com/ros/rosdistro/master/ros.key> -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] <http://packages.ros.org/ros2/ubuntu> $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update && sudo apt upgrade -y
sudo apt install ros-humble-desktop ros-dev-tools
sudo apt-get install python3-rosdep
sudo apt update && sudo apt install -y \
  build-essential \
  cmake \
  git \
  python3-colcon-common-extensions \
  python3-flake8 \
  python3-pip \
  python3-pytest-cov \
  python3-rosdep \
  python3-setuptools \
  python3-vcstool \
  wget

sudo rosdep init
rosdep update
```

I then configured some environment variables in .bashrc

```bash
echo "export ROS_DOMAIN_ID=0" >> ~/.bashrc
echo "export ROS_LOCALHOST_ONLY=0" >> ~/.bashrc
echo "source /opt/ros/humble/setup.bash" >> .bashrc
```

and tested.

First in one terminal window:

```bash
ros2 run demo_nodes_cpp talker
```

and in a second terminal window:

```bash
ros2 run demo_nodes_cpp listener
```

Now to clone to two virtual machines.  I modified  the server's netplan, according to [this post](/notebook/virtualbox/two-clones/), which helped eliminate getting an identical ip address

```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

from:

```yaml
# This is the network config written by 'subiquity'
network:
  ethernets:
    enp0s3:
      dhcp4: true
  version: 2
```

to

```yaml
# This is the network config written by 'subiquity'
network:
  ethernets:
    enp0s3:
      dhcp4: true
      dhcp-identifier: mac
  version: 2
```

This config can be modified further as needed, but since I was just getting a demo up and running, I didn't need to define static ip's

```bash
sudo netplan try
sudo netplan apply
```

Next, I shutdown the vm and made a linked clone of it

```bash
sudo shutdown now
```

I then started both the original and clone vms and checked my work:

vm 1:

```bash
ip a
```

vm2:

```bash
ip a
```

vm1:

```bash
ros2 run demo_nodes_cpp talker
```

vm2:

```bash
ros2 run demo_nodes_cpp listener
```

## Notes

* Make sure you source your .bashrc file if you change it
* Better yet, close and reopen your terminal window (or restart your ssh session)
* Even better yet, restart the PC to test how your settings are applied from startup.
