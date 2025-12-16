---
title: Hardware and Devices
summary: " "
---

## Device / driver info

```bash
lsmod
lspci -k
dmesg
lsusb
usb-devices
udevadm info
```

## Devices

```bash
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

```bash
sudo hdparm -I /dev/sda
```

if you have an NVMe device...

```bash
sudo apt install -y nvme-cli
nvme list
#sudo nvme smart-log <node_name> 
sudo nvme smart-log /dev/nvme0n1 
sudo nvme id-ctrl /dev/nvme0n1
```

### Mounting

how to mount disks to a specific folder

```bash
#list disks
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

you can get most information from lsblk if you have temporarily mounted it...

```bash
#UUID=<yourUUID> <mount_location> <filesystem>  <options>  <dump(use 0)>  <order(use 2)>
UUID=24df9215-550f-4ca0-a9f1-8f0efd2 /media/backup ext4 defaults 0 2
```

once you have edited, check by running

```bash
mount -a
```

### unlock a LUKS disk from bash

```bash
sudo apt-get install cryptsetup
```

```bash
sudo cryptsetup luksOpen /dev/<hard-drive-name> <label>
sudo mount /dev/mapper/<label> </path/to/mount/location>
```

to lock it back up:

```bash
sudo umount </path/to/mount/location>
sudo cryptsetup luksClose <label>
```

### Check unused space

first use  ```lsblk -a``` to determine if you're talking about a physical partition or a logical volume

First try parted for physical partions

```bash
sudo parted /dev/<hard-drive-name> print free
```

for example

```bash
sudo parted /dev/sda print free
```

If LVM,

```bash
sudo vgdisplay
```

this returns some useful data:

```text
  VG Name               ubuntu-vg
  System ID             
  Format                lvm2
  ...
  Act PV                1
  VG Size               <928.46 GiB
  PE Size               4.00 MiB
  Total PE              237685
  Alloc PE / Size       25600 / 100.00 GiB
  Free  PE / Size       212085 / <828.46 GiB
  ...
```

to learn about the logical volume, use

```bash
sudo lvs
```

to learn about the volume group (in Bytes), use

```bash
sudo vgs --units B
```

### Extend LVM volume

we see that my volume group is called "ubuntu-vg"

```bash
sudo lvextend -L +<amount-to-extend> /dev/mapper/ubuntu--vg-ubuntu--lv
```

update the partition 

```bash
udo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv 
```


### Recursively find storage space of a directory

```bash
du -sh /path/to/my/dir
```

list directories, one level only

```bash
du -h  --max-depth 1 /path/to/my/dir
```

### Find the free space of a drive

```bash
df -H
```

### Disk Cloning

check out dd

```bash
sudo fdisk -l /dev/sdb

sudo dd if=/dev/sda of=~/sda.dd bs=128k status=progress conv=noerror,sync
sudo dd if=/dev/sda bs=128k status=progress conv=noerror,sync | gzip -c > /sda.gz
sudo dd if=/dev/sda of=/media/danaukes/<some-uuid-here>/sda.dd bs=128k status=progress conv=noerror,sync
```

## Change Swap

you can add hard drive space to augment RAM.  This is usually set up when you install ubuntu, but it can be changed.

1. Turn off existing swap processes

    ```bash
    sudo swapoff -a
    ```

1. Resize swap

    ```bash
    #sudo fallocate -l <swapsize> /swap.img 
    sudo fallocate -l 1G /swap.img
    ```

    you can use whatever size you want in place of 1G

    if that doesn't work, use

    ```bash
    sudo dd if=/dev/zero of=/swap.img bs=1M count=4096 
    ```

1. ensure swap has the right permissions

    ```bash
    sudo chmod 600 /swap.img
    ```

1. pass the new swapfile to swap

   ```bash
   sudo mkswap /swap.img
   ```

1. Activate the swap file

   ```bash
   sudo swapon /swap.img
    ```

1. check /etc/fstab, and ensure it has this line:

    ```bash
    /swap.img none swap sw 0 0 
    ```

1. verify your swap size:

    ```bash
    free -h
    cat /etc/fstab 
    ```

## Change Swappiness

```bash
cat /etc/sysctl.conf | grep -i swappiness
```

```bash
echo "vm.swappiness = 10" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

## Read from Serial

```bash
sudo apt install -y cu
cu -l /dev/ttyACM0 -s 9600
```

To exit enter ```ctrl+a``` then ```k```, then confirm with ```y```

```bash
sudo apt install -y screen
screen /dev/ttyACM0 9600
```

## Identifying and locating USB devices

These widely used commands can be used to list and learn about connected USB devices in Linux.

```bash
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

```bash
lsusb -t
```

list all the details about a device at port 1: device 3

```bash
lsusb -v -s 1:3
```

list all the details about a vendor:product

```bash
lsusb -vd  0x03e7:0x2485 
```

## Permissions

## External Resources

* <https://devconnected.com/how-to-list-disks-on-linux/>
* <https://www.percona.com/blog/2017/02/09/using-nvme-command-line-tools-to-check-nvme-flash-health/>
* <https://stackoverflow.com/questions/454899/how-to-convert-flat-raw-disk-image-to-vmdk-for-virtualbox-or-vmplayer>
* <https://www.cyberciti.biz/faq/unix-linux-dd-create-make-disk-image-commands/>
* information on nautilus-aware mount locations: <https://gitlab.gnome.org/GNOME/gvfs/blob/master/monitor/udisks2/what-is-shown.txt>
* <https://www.cyberciti.biz/hardware/5-linux-unix-commands-for-connecting-to-the-serial-console/>
* <https://ploi.io/documentation/server/change-swap-size-in-ubuntu>
* <https://unix.stackexchange.com/questions/67806/how-to-recursively-find-the-amount-stored-in-directory>
* <https://linuxconfig.org/how-fstab-works-introduction-to-the-etc-fstab-file-on-linux>
* <https://serverfault.com/questions/174181/how-do-you-validate-fstab-without-rebooting>
* <https://linuxhint.com/how-to-mount-drive-in-ubuntu/>
* <https://linuxhint.com/du-one-level-only/>
* LVM info and resizing
    * <https://www.golinuxcloud.com/how-to-extend-lvm-partition/>
    * <https://www.redhat.com/en/blog/resize-lvm-simple>

