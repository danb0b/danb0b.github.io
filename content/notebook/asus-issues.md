---
title: ASUS Zenbook Issues
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
update-initramfs -u
```
