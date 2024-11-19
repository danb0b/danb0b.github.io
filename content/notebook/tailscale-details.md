---
title: Tailscale Details
tags:
- tailscale
- bash
- networking
summary: ""
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

to advertise as an exit node

```bash
sudo tailscale up --advertise-exit-node
```

to map a subnet

```bash
sudo tailscale up --advertise-routes=192.168.0.0/24
```

to map specific ip addresses

```bash
sudo tailscale up --advertise-routes=192.168.0.100/24,192.168.0.101/24 --advertise-exit-node
```

## Turn on HTTPS

enable magicdns
enable Https
sudo tailscale cert --cert-file=tailscale-cert.pem --key-file=tailscale-key.pem <hostname>.<tailnet>.ts.net
sudo chown <user>:<group> tailscale-*.pem


## External Resources

* <https://tailscale.com/blog/tls-certs>
* <https://tailscale.com/kb/1153/enabling-https>