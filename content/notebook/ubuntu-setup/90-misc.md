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

## Tweaking the GUI

1. Open "Extensions" and turn off desktop icons

## Update firefox settings

1. flatpak firefox settings found in ```~/.var```
2. enable home directory access through flatseal
    
    settings then found in ```~/.mozilla```

2. add "multi account containers" extension

## Update Environment Variables

1. Add folders to PATH and PYTHONPATH

## Power Options

from [here](https://fostips.com/lid-close-action-ubuntu-21-04-laptop/)

```bash
cat <<EOT | sudo tee -a /etc/systemd/logind.conf
HandleLidSwitch=lock 
HandleLidSwitchExternalPower=lock
HandleLidSwitchDocked=lock
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

