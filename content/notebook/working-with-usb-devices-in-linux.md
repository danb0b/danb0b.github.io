---
title: Working with USB devices
tags:
  - linux
  - ubuntu
  - usb
weight: 99
summary: ""
---

## Identifying and locating USB devices

These widely used commands can be used to list and learn about connected USB devices in Linux.

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
### ```lsusb```

list the device tree to get port:device

```
lsusb -t
```

list all the details about a device at port 1: device 3

```
lsusb -v -s 1:3
```

## Permissions