---
title: Unlock a LUKS partition from a file
tags:
- linux
- LUKS
- security
---

Why would you want to do this?  Sometimes, after encrypting a hard drive, you need it to auto-start.  Following these instructions, you can enable a computer with an encrypted disk to start up, de-encrypt itself, and boot.

This tutorial is derived from the following:

- <https://dradisframework.com/support/guides/customization/auto-unlock-luks-encrypted-drive.html>

```bash
lsblk  -o NAME,UUID,MOUNTPOINTS
sudo cryptsetup luksDump /dev/sda3
sudo cp /boot/initrd.img-5.15.0-58-generic /boot/initrd.img-5.15.0-58-generic.safe
```

Edit /boot/grub/grub.cfg to make a copy of your top menu entry in the advanced menu:

make sure to replace initrd img with the safe copy you just created

```bash
sudo nano /boot/grub/grub.cfg 
```

make a copy of the modified grub

```bash
sudo cp /boot/grub/grub.cfg /boot/grub/grub.cfg.mod
```

> Note: sudo update-grub will probably overwrite your changes, so don't use that.

```bash
menuentry 'Debian GNU/Linux, with Linux 4.19.0-13-amd64 (crypto safe)' --class debian --class gnu-linux --class gnu --class os {
       load_video
       insmod gzio
       insmod part_msdos
       insmod ext2
       set root='hd0,msdos1'
       search --no-floppy --fs-uuid --set=root 2a5e9b7f-2128-4a50-83b6-d1c285410145
       echo    'Loading Linux 4.19.0-13-amd64 ...'
       linux   /vmlinuz-4.19.0-13-amd64 root=/dev/mapper/dradispro-root ro  quiet
       echo    'Loading initial ramdisk ...'
       initrd  /initrd.img-4.19.0-13-amd64.safe
}
```

```bash
sudo dd if=/dev/urandom of=/boot/keyfile bs=1024 count=4
sudo chmod 0400 /boot/keyfile
sudo cryptsetup -v luksAddKey /dev/sda3 /boot/keyfile
```

find the drive the mounts at /boot (the uuid of the raw drive, not the encrypted drive.)

get its uuid

```bash
lsblk  -o NAME,UUID,MOUNTPOINTS
```

find its path

```bash
ls -l /dev/disk/by-uuid/
```

back up crypttab

```
sudo cp /etc/crypttab /etc/crypttab.bak
```

### Edit /etc/crypttab

Edit the contents of file /etc/crypttab (use the UUID of /dev/sda1 from the previous step)

```
sudo nano /etc/crypttab
```

This contents should be:

```
sda5_crypt UUID=9b7200b5-0e0a-447a-93a8-7eb8f1f4a1ee none luks,discard
```

(The _UUID_ may be different)
The changes we'll be making:
Replace the 3rd parameter ‐ `none` ‐ with `/dev/disk/by-uuid/<uuid>:/keyfile` with the UUID for the hard drive at /boot
Replace the 4th parameter ‐ `luks`‐ with `luks,keyscript=/lib/cryptsetup/scripts/passdev`
The final result:

```
sda5_crypt UUID=9b7200b5-0e0a-447a-93a8-7eb8f1f4a1ee /dev/disk/by-uuid/2a5e9b7f-2128-4a50-83b6-d1c285410145:/keyfile luks,keyscript=/lib/cryptsetup/scripts/passdev
```

In this case the UUID for our /dev/sda1 UUID was `2a5e9b7f...`.

```bash
sudo update-initramfs -u -k all
sudo reboot now
```

-------------------

sudo cryptsetup luksKillSlot /dev/nvme0n1p3 1
sudo cryptsetup luksDump /dev/nvme0n1p3
sudo nano /etc/default/grub
sudo update-grub
sudo update-initramfs -u -k all
sudo reboot now

## Other Resources

- <https://www.howtoforge.com/automatically-unlock-luks-encrypted-drives-with-a-keyfile>
- <https://linuxconfig.org/how-to-use-a-file-as-a-luks-device-key>
