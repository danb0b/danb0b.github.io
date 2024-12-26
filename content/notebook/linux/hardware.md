---
title: Hardware and Devices
summary: " "
---

## Device / driver info

```
lsmod
lspci -k
dmesg
```

## Devices

```
sudo libinput --list-devices
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
sudo apt install -y nvme-cli
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

* <https://linuxconfig.org/how-fstab-works-introduction-to-the-etc-fstab-file-on-linux>
* <https://serverfault.com/questions/174181/how-do-you-validate-fstab-without-rebooting>

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

## Disk Cloning

check out dd

```bash
sudo fdisk -l /dev/sdb

sudo dd if=/dev/sda of=~/sda.dd bs=128k status=progress conv=noerror,sync
sudo dd if=/dev/sda bs=128k status=progress conv=noerror,sync | gzip -c > /sda.gz
sudo dd if=/dev/sda of=/media/danaukes/24df9215-550f-4ca0-a9f1-8f0d666befd2/sda.dd bs=128k status=progress conv=noerror,sync
```

* <https://stackoverflow.com/questions/454899/how-to-convert-flat-raw-disk-image-to-vmdk-for-virtualbox-or-vmplayer>
* <https://www.cyberciti.biz/faq/unix-linux-dd-create-make-disk-image-commands/>

## Change Swap

* <https://ploi.io/documentation/server/change-swap-size-in-ubuntu>

## mount information

[information on nautilus-aware mount locations](https://gitlab.gnome.org/GNOME/gvfs/blob/master/monitor/udisks2/what-is-shown.txt)

## Read from Serial

from [here](https://www.cyberciti.biz/hardware/5-linux-unix-commands-for-connecting-to-the-serial-console/)

```bash
sudo apt install -y cu
cu -l /dev/ttyACM0 -s 9600
```

To exit enter tilde dot (~.)

```bash
sudo apt install -y screen
screen /dev/ttyACM0 9600
```
## Identifying and locating USB devices

These widely used commands can be used to list and learn about connected USB devices in Linux.

```
lsusb
dmesg
dmesg | less
dmesg | grep ttyUSB
usb-devices
lsblk
sudo blkid.
sudo fdisk -l
```
### ```lsusb```

list the device tree to get port:device

```
lsusb -t
```

list all the details about a device at port 1: device 3

```
lsusb -v -s 1:3
```

## Permissions