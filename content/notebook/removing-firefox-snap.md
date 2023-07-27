---
title: Removing Firefox and Snap
---

derived from [here](https://www.debugpoint.com/remove-snap-ubuntu/)

```bash
sudo snap remove --purge firefox
sudo snap remove --purge snap-store
sudo snap remove --purge lxd
sudo snap remove --purge core20
sudo snap remove --purge snapd

sudo apt remove --autoremove snapd

cat << EOT | sudo tee /etc/apt/preferences.d/nosnap.pref
Package: snapd
Pin: release a=*
Pin-Priority: -10
EOT

sudo apt update
```