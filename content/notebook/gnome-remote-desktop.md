---
title: Gnome Remote Desktop
tags:
- rdp
- ubuntu
- gnome
---

sudo apt install vino
sudo apt install winpr-utils

```
sudo systemctl restart gnome-remote-desktop.service
sudo grdctl --system rdp enable

sudo rm -rf ~gnome-remote-desktop/rdp-tls*
sudo -u gnome-remote-desktop winpr-makecert     -silent -rdp -path ~gnome-remote-desktop rdp-tls

sudo grdctl --system rdp set-tls-key /var/lib/gnome-remote-desktop/rdp-tls.key
sudo grdctl --system rdp set-tls-cert /var/lib/gnome-remote-desktop/rdp-tls.crt

sudo systemctl daemon-reload
sudo systemctl enable --now gnome-remote-desktop.service
sudo grdctl --system rdp set-credentials "name" "password"

sudo systemctl restart gnome-remote-desktop.service
sudo systemctl status gnome-remote-desktop.service
```

```
sudo ufw allow 3389
sudo ufw reload
```

https://www.mankier.com/1/grdctl

https://linuxgenie.net/install-remote-desktop-xrdp-ubuntu-24-04/
https://askubuntu.com/questions/1499789/enable-rdp-from-command-line
https://github.com/NixOS/nixpkgs/issues/266774
https://discourse.nixos.org/t/configuring-remote-desktop-access-with-gnome-remote-desktop/48023/3
https://serverfault.com/questions/1160308/certificate-for-gnome-remote-desktop


Errors:

https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/issues/12
https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/issues/161
https://github.com/FreeRDP/FreeRDP/issues/8567
https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/issues/161

sudo apt-get --reinstall install mutter mutter-common mutter-common-bin

sudo update-initramfs -u -k all
sudo ubuntu-drivers autoinstall
sudo apt purge xrdp
journalctl /usr/libexec/gnome-remote-desktop-daemon -f
