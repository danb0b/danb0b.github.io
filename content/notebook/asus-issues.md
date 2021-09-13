---
title: ASUS Zenbook Issues
tags:
  - ASUS
  - linux
  - ubuntu
---

When the hard drive is encrypted the ASUS keyboard does not load by default.

find HID modules

```
lsmod
```

add those modules to initramfs

```
sudo nano /etc/initramfs-tools/modules
```

add one per line

```
i2c_hid
hid_multitouch
hid_generic
```

update initramfs:

```
sudo update-initramfs -u -k all
```


## AMDGPU

when doing update-initramfs in kernel 5.11.0-31, there are some messages about amdgpu missing drivers

Add the following line to /etc/modprobe.d/blacklist.conf.

```
blacklist amdgpu
```

As initramfs contains modprobe configuration, update the initramfs and reboot:

```
sudo update-initramfs -u -k all
```

Check whether the driver blacklisted or not, the following command should output nothing.

```
$ lsmod | grep amdgpu
```

But this kills hdmi...
