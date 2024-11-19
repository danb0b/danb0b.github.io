---
title: Distrobox Info
summary: ""
---

sudo apt install -y distrobox
curl -s https://raw.githubusercontent.com/89luca89/distrobox/main/install | sudo sh

distrobox create --name test --image ubuntu:24.04 -a "--runtime crun"

distrobox create --image ubuntu:24.04 --home ~/homes/ubuntu-24 -n ubuntu -a "--runtime crun"



## External References

* <https://distrobox.it/>
* <https://itsfoss.com/distrobox/#1-create-a-new-container>
* <https://github.com/89luca89/distrobox/issues/1359>
* <https://linuxconfig.org/how-to-integrate-any-linux-distribution-inside-a-terminal-with-distrobox>
* <https://github.com/89luca89/distrobox/discussions/1127>