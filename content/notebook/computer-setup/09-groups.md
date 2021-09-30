---
title: Set Up Groups
---

1. add yourself to device groups

```bash
sudo usermod -aG dialout $USER
sudo usermod -aG tty $USER
```

1. reboot to take effect

```
sudo reboot 0
```