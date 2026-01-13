---
title: Korg Nano
tags:
- ros
- ubuntu
- linux
- korg
---

```bash
SUBSYSTEM=="usb", ATTR{idVendor}=="0944", ATTR{idProduct}=="010f", MODE="666"
```



```bash
sudo cp 98-korg-nano.rules /etc/udev/rules.d/
sudo chmod 644 /etc/udev/rules.d/98-korg-nano.rules
sudo udevadm control --reload-rules && udevadm trigger
```

```bash
#sudo apt install -y libasound2-dev 
#sudo apt install -y python3-pyrex
#pip3 install pyalsa
#pip3 install pygame
#pip3 install alsaseq
sudo apt install -y libjack-dev
pip3 install python-rtmidi mido
```