---
title: Removing Snap from Ubuntu
tags:
- ubuntu
- firefox
- snap
summary: " "
---


This is useful for stalled updates when installing ubuntu-desktop-minimal on a server.  the firefox snap package seems to hang.

```bash

# Common snaps
sudo snap remove --purge amazon-ssm-agent
sudo snap remove --purge firefox
sudo snap remove --purge snap-store
sudo snap remove --purge lxd
sudo snap remove --purge core20
sudo snap remove --purge core18
sudo snap remove --purge snapd
sudo snap remove --purge core18
sudo snap remove --purge core22
sudo snap remove --purge snapd

sudo apt remove --autoremove snapd

cat << EOT | sudo tee /etc/apt/preferences.d/nosnap.pref
Package: snapd
Pin: release a=*
Pin-Priority: -10
EOT

sudo apt update

rm -rf ~/snap
sudo rm -rf /snap
sudo rm -rf /var/snap
sudo rm -rf /var/lib/snapd
```

## External Resources

* <https://www.debugpoint.com/remove-snap-ubuntu/>
* <https://www.baeldung.com/linux/snap-remove-disable>