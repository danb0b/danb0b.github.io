---
title: Korg Nano
---

```
SUBSYSTEM=="usb", ATTR{idVendor}=="0944", ATTR{idProduct}=="010f", MODE="666"
```



```
sudo cp 98-korg-nano.rules /etc/udev/rules.d/
sudo chmod 644 /etc/udev/rules.d/98-korg-nano.rules
sudo udevadm control --reload-rules && udevadm trigger
```

```
sudo apt install libasound2-dev 

#sudo apt install python3-pyrex
#pip3 install pyalsa
#pip3 install pygame
pip3 install alsaseq
```