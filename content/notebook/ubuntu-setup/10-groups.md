---
title: 10-Set Up Groups
weight: 100
tags:
- ubuntu
- linux
- security
---

1. add yourself to device groups for access to some USB devices in python

```bash
sudo usermod -a -G <group1>,<group2>,... $USER
```

Example:

```bash
sudo usermod -a -G dialout,tty $USER
```

1. reboot to take effect

```bash
sudo reboot 0
```
