---
title: Port Forwarding Cheatsheet
tags:
  - ssh
weight: 99
---

```
ssh -L (localport):localhost:(remoteport) -C -N -l (username) hostname.domain -p (sshport)
```

## VNC Example

ssh into port 22 on mydynamichost.ddns.net and map the remote computer's port 5901 to my local port 59000

```
ssh -L 59000:localhost:5901 -C -N -l username mydynamichost.ddns.net -p 22
```
