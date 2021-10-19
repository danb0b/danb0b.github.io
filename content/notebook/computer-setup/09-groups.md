---
title: Set Up Groups
weight: 9
---

1. add yourself to device groups for access to some USB devices in python

```bash
sudo usermod -aG dialout $USER
sudo usermod -aG tty $USER
```

1. reboot to take effect

```
sudo reboot 0
```