---
title: Post-Install Miscellaneous Steps
weight: 900
tags:
- ubuntu
- linux
- gnome
- python
- ssh
---

## Install gnome tweaks

```bash
sudo apt install gnome-tweaks
```

## Tweaking the GUI

1. Open "Extensions" and turn off desktop icons

## Update firefox settings

1. flatpak firefox settings found in ```~/.var```
2. enable home directory access through flatseal
    
    settings then found in ```~/.mozilla```

2. add "multi account containers" extension

## Update Environment Variables

1. Add folders to PATH and PYTHONPATH

## Configure /etc

* /etc/netplan (if applicable)
* /etc/hosts
* /etc/network-manager configs

## Configure SSH

## Configure VSCode

## Power Options

from [here](https://fostips.com/lid-close-action-ubuntu-21-04-laptop/)

```bash
cat <<EOT | sudo tee -a /etc/systemd/logind.conf
HandleLidSwitch=lock 
HandleLidSwitchExternalPower=lock
HandleLidSwitchDocked=ignore #when it's docked, leave it unlocked
EOT
```

save your work and then run

```bash
systemctl restart systemd-logind.service
```

## External References

* [top-things-to-do-after-installing-ubuntu-1504-unixmen](https://www.unixmen.com/top-things-installing-ubuntu-14-1014-0413-1013-0412-1012-04/)


## Install drivers for docking hub

Steps found [here](https://forums.lenovo.com/t5/Ubuntu/ThinkPad-Hybrid-USB-C-with-USB-A-Dock-for-linux/td-p/4315328)

<https://www.synaptics.com/products/displaylink-graphics/downloads/ubuntu>

## Remove

There were errors related to newer kernels in 23.04

```bash
sudo displaylink-installer uninstall 
```

## Fix wpasupplicant issue

Edit sources

```bash
cat <<EOT | sudo tee -a /etc/apt/sources.list
deb http://old-releases.ubuntu.com/ubuntu/ impish main restricted universe multiverse
deb http://old-releases.ubuntu.com/ubuntu/ impish-updates main restricted universe multiverse
deb http://old-releases.ubuntu.com/ubuntu/ impish-security main restricted universe multiverse
EOT
```

Then run the following lines

```bash
sudo apt update && \
sudo apt --allow-downgrades install wpasupplicant=2:2.9.0-21build1 && \
sudo apt-mark hold wpasupplicant
```

* <https://devicetests.com/fix-hotspot-connection-issues-ubuntu-22-04-1-lts-android-11>
* https://askubuntu.com/questions/580433/how-can-i-allow-ap-hotspot-in-ufw-ubuntu-14-04


This enables the wifi devices to communicate and get ip addresses over dhcp:

```bash
sudo ufw allow to any port 53
sudo ufw allow to any port 67 proto udp
sudo ufw allow to any port 68 proto udp
```

* <https://devicetests.com/fix-ubuntu-2204-hotspot-connection-issues> 


Add passthrough between wifi and ethernet devices, for example:


```bash
sudo ufw allow in on wlp1s0
sudo ufw route allow out on enx0050b6bd4061
sudo ufw route allow out on enx00b56d06277a
```

## Add a tiling window manager

https://extensions.gnome.org/extension/3733/tiling-assistant/