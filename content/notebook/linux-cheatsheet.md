---
title: Linux / Bash Cheatsheet
summary: Collected commands, tips, and tricks for working headless in Ubuntu
tags:
  - linux
  - bash
  - ubuntu
weight: 1
---

## Find Kernel version

```
uname -r
```

More detailed information 
```bash
uname -a
```

## Device / driver info

```
lsmod
lspci -k
dmesg
```

## Crontab

how to run python scripts: <https://www.geeksforgeeks.org/how-to-schedule-python-scripts-as-cron-jobs-with-crontab/>

create a new python script

```python
#!/usr/bin/env python3
import time
import os
with open(os.path.expanduser('~/crontest.txt'),'a') as f:
    f.write(time.ctime()+'\n')
```

```bash
chmod +x test.py
```


```bash
crontab -e
```

```bash
# m h  dom mon dow   command
* * * * * $HOME/test.py
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
ifconfig <network interface> down
ifconfig <network interface> up
```

```
ip link
```

```
ip addr
```

## APT / dpkg

```
sudo apt list --installed <package-name-start*>
```

```
sudo apt --reinstall install <package>
```

```bash
dpkg --list | grep <package-name-fragment>
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

## Login, Logout, Restart

```bash
sudo reboot now
sudo shutdown now
gnome-session-quit
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

## Users, groups

From: 

* <https://linuxize.com/post/how-to-add-and-delete-users-on-ubuntu-20-04/>
* <https://askubuntu.com/questions/410244/is-there-a-command-to-list-all-users-also-to-add-delete-modify-users-in-the>

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
    
### Remove User

```bash
sudo deluser --remove-home username
```

### Force new password

```bash
passwd --expire <username_here>
```

### Expire / unexpire

from [here](https://askubuntu.com/questions/282806/how-to-enable-or-disable-a-user)

Expire Account

Let the account expire to disallowing a user from logging in from any source including ssh:

```bash
# disallow peter from logging in
sudo usermod --expiredate 1 peter
```

This is how you can reenable that account:

```bash
# set expiration date of peter to Never
sudo usermod --expiredate "" peter
```


### List all users / groups

users:

```bash
cut -d: -f1 /etc/passwd
getent passwd
```

groups:

```bash
cut -d: -f1 /etc/group
getent group
```

### find out who is logged on

```bash
users
who
```

## Update Distro

Based on [this link](https://vitux.com/how-to-upgrade-ubuntu-20-04-to-21-04/)

1. Might as well be fully updated first

    ```bash
    sudo apt update
    sudo apt upgrade
    sudo shutdown -r now
    ```

1. edit which upgrade you want to do (lts or normal)

    ```bash
    sudo nano /etc/update-manager/release-upgrades
    ```

    change ```prompt=lts``` to ```prompt=normal```
    
1. run updater

    ```bash
    do-release-upgrade
    ```
    
    you may need to indicate what to do with specific config files that get updated.
    
1. Restart

    ```bash
    sudo shutdown -r now
    ```
    

## get ip info

from [here](https://www.cyberciti.biz/faq/how-to-find-my-public-ip-address-from-command-line-on-a-linux/)

```bash
ifconfig
host myip.opendns.com resolver1.opendns.com
dig @resolver4.opendns.com myip.opendns.com +short
```

### get mac

<https://www.lifewire.com/find-a-mac-address-using-an-ip-address-818132>

```bash
arp -a <ip address>
```

### Wifi Scanning

```
nmcli d wifi
```

## sudo

to run something as root

```bash
sudo <command> [command options]
```

to run interactively as root

```bash
sudo -i
```

to run something as someone else

```bash
sudo -i -u <username>
```

run ```exit``` to leave that session

## Show all manually-installed packages

```bash
apt-mark showmanual
```

## close bash without saving history

```bash
unset HISTFILE && exit
```

## Package Management

### List repositories

```bash
apt policy
```

### Remove a repository

```bash
sudo add-apt-repository --remove ppa:PPA_Name/ppa
```

## Misc
### Count files in bash

source: <https://devconnected.com/how-to-count-files-in-directory-on-linux/>

```bash
ls | wc -l
```

### How to find .desktop file location for a particular application

For example, if "Image Viewer" is in the name of the icon:

```
find / -name '*.desktop' -exec grep -H 'Image Viewer' {} \; 2>/dev/null
```

derived from [here](https://askubuntu.com/questions/1160737/how-to-find-desktop-file-location-for-a-particular-application):

Some default locations listed [here](https://askubuntu.com/questions/1146307/which-desktop-files-belong-where):
```
/usr/share/applications/gnome-terminal.desktop
~/.local/share/applications/gnome-terminal.desktop
~/.config/gnome-panel/launchers/gnome-terminal.desktop
~/.gnome/apps/gnome-terminal.desktop
```

## Learn about your hardware

### Get DMI/BIOS information

```bash
sudo dmidecode 
sudo dmidecode -t0 # BIOS
sudo dmidecode -t1 # System
sudo dmidecode -t2 # Board
sudo dmidecode -t3 # Enclosure or Chassis
sudo dmidecode -t4 # Processor
sudo dmidecode -t1 # System
```


## Trash


Files can be stuck in ~/.local/share/Trash/expunged when you delete from Nautilus a folder that belongs to you, but contains files which are belong to another user, and it is tricky for Nautilus to handle this situation correctly. To delete them try to use:

```bash
sudo -i
rm -rv /home/<desired_user_name>/.local/share/Trash/expunged/*
exit
```

## octal file permissions

```bash
stat /path/to/filename
```

```bash
stat -c '%A %a %n' /path/to/filename
```

## Drives


### Hard drive information

* <https://devconnected.com/how-to-list-disks-on-linux/>
* <https://www.percona.com/blog/2017/02/09/using-nvme-command-line-tools-to-check-nvme-flash-health/>

list disks with ```lsblk```

```bash
lsblk -f #list filesystem details
lsblk -t #show topology
lsblk -i # use ascii
lsblk -o NAME,UUID # show specific columns
sudo lshw -class disk
sudo fdisk -l
sudo hwinfo --disk
ls -l /dev/disk/by-path
ls -l /dev/disk/by-id
```

get drive information:

```
sudo hdparm -I /dev/sda
```

if you have an NVMe device...

```
sudo apt install nvme-cli
nvme list
#sudo nvme smart-log <node_name> 
sudo nvme smart-log /dev/nvme0n1 
sudo nvme id-ctrl /dev/nvme0n1
```

### Mounting

From [here](https://linuxhint.com/how-to-mount-drive-in-ubuntu/)

```bash
##list disks
sudo fdisk -l
#if you know the disk you want info about:
sudo fdisk -l /dev/sdd 
sudo mount /dev/sdd1 /media/backup
# unmount
sudo umount /media/backup
# unmount all
sudo umount -a
# force unmount
sudo umount -f /media/backup
```

### mounting with fstab

- <https://linuxconfig.org/how-fstab-works-introduction-to-the-etc-fstab-file-on-linux>
- <https://serverfault.com/questions/174181/how-do-you-validate-fstab-without-rebooting>

you can get most information from lsblk if you have temporarily mounted it...

```bash
#UUID=<yourUUID>                           <mount_location> <filesystem>  <options>  <dump(use 0)>  <order(use 2)>
UUID=24df9215-550f-4ca0-a9f1-8f0efd2  /media/backup    ext4          defaults   0       2
```

once you have edited, check by running

```bash
mount -a
```

## Recursively find storage space of a directory

from [here](https://unix.stackexchange.com/questions/67806/how-to-recursively-find-the-amount-stored-in-directory)

```bash
du -sh /path/to/my/dir
```

list directories, one level only, from [here](https://linuxhint.com/du-one-level-only/)

```bash
du -h  --max-depth 1 /path/to/my/dir
```
## Find the free space of a drive

```bash
df -H
```

## Recursively list files

from [here](https://www.cyberciti.biz/faq/how-to-show-recursive-directory-listing-on-linux-or-unix/)
```bash
tree /path/to/dir
```

## Recursively chown

from [here](https://devconnected.com/how-to-chown-recursive-on-linux/)

```bash
#chown -R <owner> <folder_1> <folder_2> ... <folder_n>
chown -R user /home/user
```

## Print your environment variables

```bash
printenv | grep ROS
```

## mount information


[information on nautilus-aware mount locations](https://gitlab.gnome.org/GNOME/gvfs/blob/master/monitor/udisks2/what-is-shown.txt)


## Read from Serial

from [here](https://www.cyberciti.biz/hardware/5-linux-unix-commands-for-connecting-to-the-serial-console/)

```bash
sudo apt install cu
cu -l /dev/ttyACM0 -s 9600
```

To exit enter tilde dot (~.)

```bash
sudo apt install screen
screen /dev/ttyACM0 9600
```
## tail

From [here](https://www.howtogeek.com/481766/how-to-use-the-tail-command-on-linux/)

see the last few lines

```bash
#tail -100 <filename>
tail -100 history.txt
```

see real-time changes to files as they get appended:

```bash
tail -f history.txt
```

see line 196-200 of a file

```bash
head -200 history.txt | tail -5
```

## More

see [this page](/bookmarks/linux-cheatsheet-links/) for more links


## List login times including boots

list login dates / times, users, etc

```bash
last
```

## Boot Information

more info [here](https://askubuntu.com/questions/995711/where-can-i-find-the-boot-log)

```bash
journalctl --list-boots 
```

Will list all recent boots

```bash
journalctl --boot=<boot id>
```

To just get information about the most recent boot, use

```bash
journalctl -b
```

## Accidentally deleted sudoers

use pkexec to do things you would normally do with sudo, like

pkexec cp /path/to/sudo/backup /etc/sudoers

great advice from here: <https://askubuntu.com/questions/438123/accidentally-deleted-etc-sudoers-file>


## Networking

```bash
nm-connection-editor
```