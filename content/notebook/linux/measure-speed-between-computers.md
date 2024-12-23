---
title: Measuring Speed Between Computers
tags:
- bash
- linux
- networking
summary: " "
---


sudo apt install -y iperf


computer 1: 

```bash
iperf -s
```

Computer 2: 

```bash
iperf -c <other-computer-ip-or-hostname>
```

<https://superuser.com/questions/1275043/measure-bandwidth-between-two-computer-in-a-lan>
