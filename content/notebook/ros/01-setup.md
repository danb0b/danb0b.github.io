---
---

## Introduction

This section discusses how to prepare a computer for installing ROS.  Because many students don't have a spare 

## Nomenclature

If you are installing a linux virtual machine on your windows computer, your windows computer is called the "host", and the linux virtual machine is called the "guest"

## Host Computer Installation

You will need some packages installed on the host side to communicate with your guest(virtual) machine

1. Install Python, preferably via the [Anaconda](https://www.anaconda.com/products/individual) distribution
    1. You'll need some additional packages.  From a command prompt:

        ```
        pip install service_identity roslibpy
        ```
1. C/C++ Compiler (optional).  Only required if you will be installing python packages on Windows that need to be compiled.
1. Install [Virtualbox](https://www.virtualbox.org/).  This tutorial was written for Virtualbox 6, though I don't anticipate major functionality changes between neighboring versions.  Install the latest version.
1. Install the virtualbox extension pack as well
1. Install [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) for networked ssh acess

## Download Ubuntu

You probably want [Ubuntu 18.04 (LTS)](http://releases.ubuntu.com/18.04.4/) desktop edition.  Make sure you download an .iso file so that the virutal machine can load it.

**Note:** The ROS version you want to use impacts which Ubuntu version you should select.  They are paired together.

## Creating the Guest Machine

The next steps outline how to go about creating a Virtual Machine similar to the one used in this tutorial.  

1. Create Virtual Machine
    * 4Gb Ram
    * 50Gb HD, flexible size option
    * 1-2 cpus
    * load ubuntu 18.04 iso
1. Install Ubuntu
    * minimum install
    * no 3rd party drivers 
    * no downloads during install
    * username: idealab
    * pw: idealab
    * sign in automatically
1. take a snapshot of the virtual machine at this point.  If anything goes wrong you can go back to this point

## Set up the Virtual Machine to prepare for ROS install 

**Note:** All these steps should be run within the guest.

**Hint:** To open up a terminal, remember the handy keyboard-based shortcut of ```ctrl+alt+t```


1. install guest additions
    1. First, run this in the terminal

        ```bash
        sudo apt install -y virtualbox-guest-utils virtualbox-guest-dkms
        ```
    1. Install the virtualbox guest additions cd from the guest os window and select run when the button pops up.
    1. let it run
    1. eject the cd from the virtualbox host menu
    1. Restart guest computer (using the guest menu in the top right corner)

1. Install other packages

    ```bash
    #update repository
    sudo apt update
    #visual package manager
    sudo apt install -y synaptic
    #ssh access
    sudo apt install -y openssh-server
    #python editor
    sudo apt install -y spyder3
    #ifconfig command and other networking tools
    sudo apt install net-tools
    #misc
    sudo apt install -y curl
  	#python packages
  	sudo apt install -y python3-serial python3-pip
    ```

1. Take another Snapshot

## Installing ROS

Follow the detailed installation instructions at <https://wiki.ros.org/melodic/Installation/Ubuntu>, or follow the  condensed instructions in the next section.

## Guest Network Setup

1. Power down your guest machine from within the guest OS (top right corner of the screen)
1. Once powered down, in your host machine, change the virtualbox network settings to "bridged adapter" mode
1. Assign a custom MAC address to the guest in the advanced preferences menu.  This will make your virtual machine easier to identify for further network setup
    * You can use something like 000000000001 to make it easy to remember, but **never use the same MAC address for multiple machines on the same network**.  It is supposed to be a unique identifier.
1. Start the guest machine again
1. Find the ip address of ethernet port in the terminal

    ```bash
    #sudo apt install net-tools
    ifconfig -v
    ```

1. this will return information about each networking device, that looks like this:

    ```
    enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 192.168.0.17  netmask 255.255.255.0  broadcast 192.168.0.255
            inet6 2600:8800:2281:3600:a6d7:41a9:9d6b:e48b  prefixlen 64  scopeid 0x0<global>
            inet6 fe80::7804:5434:c83:a827  prefixlen 64  scopeid 0x20<link>
            inet6 2600:8800:2281:3600:588c:62a0:442a:d6ce  prefixlen 64  scopeid 0x0<global>
            ether 08:00:27:00:80:00  txqueuelen 1000  (Ethernet)
            RX packets 47127  bytes 47300474 (47.3 MB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 13563  bytes 1385399 (1.3 MB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 117914  bytes 20197993 (20.1 MB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 117914  bytes 20197993 (20.1 MB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    ```
    
1. The value you want is the "inet" value under, in this case, enp0s3, or 192.168.0.17 in our case.  Remember this value, this is how you will communicate with your virtual pc

## Assign a static ip address (optional)

You can do this in your router or within the guest machine; this will enable you to communicate with this machine at a known address.

### Option 1: Router-specific instructions

Please see the router specific instructions for reserving a specific IP address (using the guest machine's custom MAC address) using DHCP.  You must have administrator access to your router

### Option 2: Within the Guest:

Open up the network configuration (top right hand corner of the screen near power) and follow the menu system to assign a custom IP4 address to your ethernet controller.  You should be comfortable with networking concepts and have a firm understanding of your network topology before modifying this setting, or other computers will no longer be able to communicate with this computer.
