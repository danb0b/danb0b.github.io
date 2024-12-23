---
title: Simple Netplan Config
tags:
  - netplan
  - ubuntu
  - networking
summary: " "
---



## Example

> update enp0s3 to match your ethernet interface

<p></p>

> update ip4 address to match an available address

### Backup your config

```bash
sudo cp /etc/netplan/01-network-manager-all.yaml /etc/netplan/01-network-manager-all.yaml.bak
sudo nano /etc/netplan/01-network-manager-all.yaml
```

### Update your config

edit the file, making sure to update the desired ip address, the name of the interface

```
network:
    version: 2
    ethernets:
        eno1:
            addresses:
            - 192.168.0.120/24
            dhcp4: no
            dhcp6: no
            nameservers:
                addresses:
                - 1.1.1.1
                - 8.8.8.8
                - 8.8.4.4
            optional: false
            routes:
                - to: default
                  via: 192.168.0.1
    wifis:
        wlp2s0:
            dhcp4: no
            dhcp6: no
            addresses:
            - 192.168.0.121/24
            nameservers:
                addresses:
                - 1.1.1.1
                - 8.8.8.8
                - 8.8.4.4
            access-points:
                "<enter-your-ssid>":
                    password: "<enter-your-password>"
```

## External References


* <https://netplan.io/examples>
* <https://ubuntu.com/core/docs/networkmanager/networkmanager-and-netplan>
