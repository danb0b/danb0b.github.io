---
title: install node
tags:
- nodejs
- node
- npm
---

<https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04>

```bash
cd ~/Downloads
curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs
node -v
```