---
title: Simple Netplan Config
tags:
  - netplan
  - ubuntu
  - networking
---

## Configs

Are usually found in /etc/netplan/

## Usage

to test your config for 120 seconds

```bash
sudo netplan try
```

to apply a config without testing:

```bash
sudo netplan apply
```

### Backup your config

```bash
sudo cp /etc/netplan/01-network-manager-all.yaml /etc/netplan/01-network-manager-all.yaml.bak
sudo nano /etc/netplan/01-network-manager-all.yaml
```

### Update your config

edit the file, making sure to update the desired ip address, the name of the interface

```yaml
network:
    version: 2
    ethernets:
        eno1: #change to your adapter name
            addresses:
            - 192.168.0.120/24 # the ip address for your enthernet adapter
            dhcp4: no # disable dhcp for ipv4
            dhcp6: no # disable dhcp for ipv6
            nameservers: # dns servers
                addresses:
                - 1.1.1.1 # cloudflare
                - 8.8.8.8 # google
                - 8.8.4.4 # google
                #- 192.168.0.1 #local
            optional: false
            routes:
                - to: default
                  via: 192.168.0.1
    wifis:
        wlp2s0: #change to your adapter name
            addresses:
            - 192.168.0.121/24 # the hard coded ip address for your wifi
            dhcp4: no # disable dhcp for ipv4
            dhcp6: no # disable dhcp for ipv6
            nameservers: # dns servers
                addresses:
                - 1.1.1.1 # cloudflare
                - 8.8.8.8 # google
                - 8.8.4.4 # google
                #- 192.168.0.1 #local
            access-points:
                "<enter-your-ssid>":
                    password: "<enter-your-password>"
```

## External References

* <https://netplan.io/examples>
* <https://ubuntu.com/core/docs/networkmanager/networkmanager-and-netplan>
