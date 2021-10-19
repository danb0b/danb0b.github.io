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

From <https://fostips.com/lid-close-action-ubuntu-21-04-laptop/>

edit ```/etc/systemd/logind.conf``` to configure power options such as lid closing opening, 

```
HandleLidSwitch=ignore
HandleLidSwitchExternalPower=ignore
HandleLidSwitchDocked=ignore
```

1. Restart Service

```bash
systemctl restart systemd-logind.service
```

## Users

From: <https://linuxize.com/post/how-to-add-and-delete-users-on-ubuntu-20-04/>

1. Create a new user

    ```bash
    sudo adduser username
    ```

1. Find groups associated with current user:

    ```bash
    groups $USER
    ```

1. Add new user to new groups

    ```bash
    sudo usermod -aG adm username
    sudo usermod -aG sudo username
    #...
    ```
