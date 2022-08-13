---
title: Simple Netplan Config
tags:
  - netplan
  - ubuntu
  - networking
---

## Example

* update enp0s3 to match your ethernet interface
* update ip4 address to match an available address

```bash
sudo cp /etc/netplan/01-network-manager-all.yaml /etc/netplan/01-network-manager-all.yaml.bak
sudo nano /etc/netplan/01-network-manager-all.yaml
```

edit the file, making sure to update the desired ip address, the name of the interface

```
network:
    version: 2
    ethernets:
        enp0s3:
            addresses:
            - 192.168.0.121/24
            dhcp4: false
            nameservers:
                addresses:
                - 1.1.1.1
                - 8.8.8.8
                - 8.8.4.4
            optional: false
            routes:
                - to: default
                  via: 192.168.0.1
```

