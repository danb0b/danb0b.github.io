---
title: Tailscale Details
---


from [here](https://tailscale.com/kb/1103/exit-nodes/)

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
