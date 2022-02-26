---
title: Simple Netplan Config
tags:
  - netplan
  - ubuntu
  - networking
---

## Example

* update eno1 to match your ethernet interface
* update ip4 address to match an available address

```
network:
    version: 2
    ethernets:
        eno1:
            addresses:
            - 192.168.0.111/24
            dhcp4: false
            nameservers:
                addresses:
                - 8.8.8.8
            optional: false
```
