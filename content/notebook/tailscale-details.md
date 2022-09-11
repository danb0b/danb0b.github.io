---
title: Tailscale Details
---


* from [here about exit nodes](https://tailscale.com/kb/1103/exit-nodes/)
* and [subnets](https://tailscale.com/kb/1019/subnets/)

## IP Forwarding

```bash
echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.conf
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p /etc/sysctl.conf
```

## Exit Node

```bash
sudo tailscale up --advertise-exit-node
```

sudo tailscale up --advertise-routes=192.168.0.0/24

sudo tailscale up --advertise-routes=192.168.0.0/24 --advertise-exit-node
