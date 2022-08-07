---
title: Enable UFW
tags:
- security
- firewall
- ubuntu
- linux
weight: 190
---

To turn on UFW,

```bash
sudo ufw allow 22
sudo ufw enable
sudo ufw status
sudo systemctl enable ufw
sudo systemctl start ufw
```