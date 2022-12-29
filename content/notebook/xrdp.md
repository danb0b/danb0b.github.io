---
title: RDP to another computer
---

Derived from [here](https://linuxconfig.org/ubuntu-22-04-remote-desktop-access-from-windows-10)

sudo apt update
sudo apt install xrdp

sudo systemctl enable --now xrdp
sudo ufw allow from any to any port 3389 proto tcp

1. open remmina

1. enter the remote server name

1. Select the default Xorg

1. Select "Dynamic Resolution Update" icon from the left panel.
