---
title: UFW -- Uncomplicated Firewall
tags:
- security
- firewall
- ubuntu
- linux
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

## Adding exceptions

```bash
sudo ufw allow <port number or service name>
sudo ufw status numbered
sudo ufw reset
sudo ufw delete <number>
```

## Specific Services

### SSH

```bash
sudo ufw allow 22/tcp
# or
sudo ufw allow ssh
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

## External references

* <https://askubuntu.com/questions/580433/how-can-i-allow-ap-hotspot-in-ufw-ubuntu-14-04>
