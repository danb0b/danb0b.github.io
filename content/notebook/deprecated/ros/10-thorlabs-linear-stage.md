---
title: Using the Thorlabs linear stage
weight: 100
tags:
- ros
- ubuntu
- linux
- thorlabs
summary: " "
---

## Introduction

These instructions are for loading and running the thorlabs linear stage in ROS.  This is not yet finished

## Instructions

1. In the host virtualbox settings, add a filter for the  thorlabs usb device.
1. open virtualbox
1. clone thorlabs linear stage code

    ```bash
    cd ~/code
    git clone https://github.com/idealabasu/code_devices_thorlabs_linear_stage.git
    ```

1. add rules to linux system.  These are located

    ```txt
    SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="faf0", MODE="666"
    ```

    ```bash
    cd ~/code/code_devices_thorlabs_linear_stage
    sudo cp 99-thorlabs.rules /etc/udev/rules.d
    sudo chmod 644 /etc/udev/rules.d/99-thorlabs.rules
    sudo udevadm control --reload-rules && udevadm trigger
    ```

1. clone idealab tools (if not already done)

    ```bash
    git clone https://github.com/idealabasu/code_idealab_tools.git
    ```

1. add git-based packages to python path

    ```bash
    echo "export PYTHONPATH=\$PYTHONPATH:~/code/code_idealab_tools/python" >> ~/.bashrc
    source ~/.bashrc
    ```

1. add git-based packages to python path

    ```bash
    echo "export PYTHONPATH=\$PYTHONPATH:~/code/code_devices_thorlabs_linear_stage/python" >> ~/.bashrc
    source ~/.bashrc
    ```

## Old steps

This is not necessary to do in Linux, as the above works with the pySerial package.  You can use the ftd2xx package in windows though.

1. install ftd2xx (windows-only)

```bash
#sudo apt update
#sudo apt install
pip3 install ftd2xx
```

1. (old) download ftd2xx drivers(see downloads below)

```bash
mkdir ~/drivers
cd ~/drivers
mkdir libftd2xx-x86_64-1.4.8
cd libftd2xx-x86_64-1.4.8
wget https://www.ftdichip.com/Drivers/D2XX/Linux/libftd2xx-x86_64-1.4.8.gz
tar -xvzf libftd2xx-x86_64-1.4.8.gz
cd release
cd build
sudo cp libftd2xx.* /usr/local/lib
sudo chmod 0755 /usr/local/lib/libftd2xx.so.1.4.8
sudo ln -sf /usr/local/lib/libftd2xx.so.1.4.8 /usr/local/lib/libftd2xx.so
echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/lib:/usr/lib:/usr/local/lib" >> ~/.bashrc
source ~/.bashrc
```

<!--
1. install pyusb
```bash
pip3 install pyusb
```

1. clone thorpy
```bash
git clone https://github.com/UniNE-CHYN/thorpy.git
```
-->

### Old Downloads

| driver | internal link                                                                                                   | external link                                                                 |
|:-------|:----------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| FTD2XX | [link](https://drive.google.com/open?id=1yfmYgPryiEtYfCHBIN3gfNWX0J58mTWm&authuser=daukes@asu.edu&usp=drive_fs) | [link](https://www.ftdichip.com/Drivers/D2XX/Linux/libftd2xx-x86_64-1.4.8.gz) |
