---
title: linux cheatsheet
tags:
  - linux
  - ubuntu
---

## Find Kernel version

```
uname -r
```


## Device / driver info

```
lsmod
lspci -k
dmesg
```

## search path

.bashrc holds path variables.

## GUI

ctrl-h hides and shows "dot" files in nautilus like ```.config``` or ```.ssh/```

## Password

```
sudo passwd <username>
```

## Networking

```
ifconfig
```

```
ifconfig up [deviceid]
```

```
ip link
```

```
ip addr
```

## APT

```
sudo apt list --installed <packa*>
```

```
sudo apt --reinstall install <package>
````

## Devices

```
sudo libinput --list-devices
```
