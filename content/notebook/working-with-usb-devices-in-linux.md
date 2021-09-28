---
title: Working with USB devices
tags:
  - linux
  - ubuntu
  - usb
---

# Identifying and locating USB devices

These widely used commands can be used to list connected USB devices in Linux.

```
lsusb
dmesg
dmesg | less
dmesg | grep ttyUSB
usb-devices
lsblk
sudo blkid.
sudo fdisk -l
```

list all the details about a device at port 1: device 3

```
lsusb -v -s 1:3
```

