---
title: Post-Install Cleanup steps
weight: 890
tags:
- ubuntu
- linux
---

```bash
sudo apt update #update repositories
sudo apt install -f #fix broken packages
sudo apt upgrade -y #install any updates
sudo snap remove firefox # just to check
sudo apt autoremove -y #remove unused packages
sudo apt clean
sudo reboot 0 # to restart immediately
```