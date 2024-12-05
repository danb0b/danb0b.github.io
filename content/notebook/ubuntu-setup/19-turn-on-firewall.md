---
title: Enable UFW
tags:
- security
- firewall
- ubuntu
- linux
weight: 190
summary: " "
---

To turn on UFW,

```bash
sudo ufw allow 22
sudo ufw enable
sudo ufw status
sudo systemctl enable ufw
sudo systemctl start ufw
```

## Specific Services

### SSH

```bash
sudo ufw allow 22
```

### Samba

```bash
sudo ufw allow Samba
```

### syncthing

```bash
sudo ufw allow syncthing
sudo ufw allow syncthing-gui
```

### dnsmasq and dhclient

for enabling wifi bridging in ubuntu

```bash
sudo ufw allow to any port 53
sudo ufw allow to any port 67 proto udp
sudo ufw allow to any port 68 proto udp
```

<https://askubuntu.com/questions/580433/how-can-i-allow-ap-hotspot-in-ufw-ubuntu-14-04>

### Wireguard

```bash
sudo ufw allow 51820/udp
```

### Unknown / Unused

```bash
sudo ufw allow 1701/tcp
sudo ufw allow 9901/tcp
sudo ufw allow 50000
```

