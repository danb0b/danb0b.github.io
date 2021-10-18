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
```

## Devices

```
sudo libinput --list-devices
```
## Find/Replace

To change the file in place:

```
sed -i "s/regex/replace/" file
```

or

```
sed -i "s|regex|replace|" file
```

To copy output to a new file

```
sed "s/regex/replace/" filein > fileout
```

List all kernel images installed:

```
$ dpkg --list | grep linux-image
```

## Ubuntu Specific

edit ```/etc/systemd/logind.conf``` to configure power options such as lid closing opening, 

```
HandleLidSwitch=ignore
HandleLidSwitchExternalPower=ignore
HandleLidSwitchDocked=ignore
```
## Users

https://linuxize.com/post/how-to-add-and-delete-users-on-ubuntu-20-04/

```bash
sudo adduser username
```

```
groups $USER
```

```bash
sudo usermod -aG adm username
sudo usermod -aG dialout username
sudo usermod -aG cdrom username
sudo usermod -aG floppy username
sudo usermod -aG sudo username
sudo usermod -aG audio username
sudo usermod -aG dip username
sudo usermod -aG video username
sudo usermod -aG plugdev username
sudo usermod -aG netdev username
sudo usermod -aG lxd username
```
