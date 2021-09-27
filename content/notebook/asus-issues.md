---
title: ASUS Zenbook Issues
tags:
  - ASUS
  - linux
  - ubuntu
---

When the hard drive is encrypted the ASUS keyboard does not load by default.

find HID modules

```
lsmod
```

add those modules to initramfs

```
sudo nano /etc/initramfs-tools/modules
```

add one per line

```
#amdgpu 
asus_wmi 
asus_nb_wmi
atkbd 
dm_crypt 
ext4 
fat 
i2c_hid 
i8042
ohci_pci
xhci_pci
xhci_pci_renesas
edac_mce_amd
kvm_amd
kvm
serio_raw
usbcore
uhci_hcd
ehci_hcd
usbhid
```

update initramfs:

```
sudo update-initramfs -u -k all
```


## AMDGPU

when doing update-initramfs in kernel 5.11.0-31, there are some messages about amdgpu missing drivers

Add the following line to /etc/modprobe.d/blacklist.conf.

```
blacklist amdgpu
```

As initramfs contains modprobe configuration, update the initramfs and reboot:

```
sudo update-initramfs -u -k all
```

Check whether the driver blacklisted or not, the following command should output nothing.

```
$ lsmod | grep amdgpu
```

But this kills hdmi...

## RECOMPILE YOUR KERNEL

1. open ```software-properties-gtk``` and enable source code
1. Follow instructions to [build your own kernel](https://wiki.ubuntu.com/Kernel/BuildYourOwnKernel)

    1. get dependencies
    1. get source

        ```
        apt source linux-image-unsigned-5.11.0-36-generic 
        ```

    1. update configs
    
        ```
        chmod a+x debian/rules
        chmod a+x debian/scripts/*
        chmod a+x debian/scripts/misc/*
        LANG=C fakeroot debian/rules clean
        LANG=C fakeroot debian/rules editconfigs # you need to go through each (Y, Exit, Y, Exit..) or get a complaint about config late
        ```

    1. Use the advice from [here](https://www.mail-archive.com/ubuntu-bugs@lists.ubuntu.com/msg5955393.html), update yoru configuration (don't uncheck "support for uevent")

        
        ```
        ASUS UM425UA internal keyboard doesn't work on a "cold boot" (first 
        power-on). It activates only after restart.
          I noticed it when tried to boot live image of Ubuntu 20.04.3
          This problem probably appeared with kernel version 5.9 or 5.10 because with 
        Ubuntu 20.04.2 live image (Linux 5.8) keyboard loads fine. Tried kernel 5.14 
        and it's still affected.
          I tried to recompile kernels 5.11 & 5.13 with SERIO_I8042 set as a module (as 
        suggested in an Arch Linux bug report) and keyboard now works from the first 
        start.
          
          In "make config" the changes are:
          Device Drivers ->
            > Generic Driver Options -> [ ] Support for uevent #may slowdown boot, 
        needed only for U14.04
            > Input device support
               > Keyboards -> [M] AT keyboard
               > Hardware I/O ports -> [M] i8042 PC Keyboard controller
          
          It changed such lines in config:
          CONFIG_KEYBOARD_ATKBD=m
          CONFIG_SERIO_I8042=m
          CONFIG_SERIO_LIBPS2=m
          
          References:
          https://bugs.archlinux.org/task/70384
          https://ubuntuforums.org/showthread.php?t=2459149
          
        https://linux.org/threads/asus-zenbook-14-um425ua-keyboard-not-respond-during-cold-boot.33738/#post-133830
          
          P.S. Other option which helped me was a GRUB parameter "i8042.reset=1" but it 
        had a positive effect only with kernel 5.11
        ```

    1. These changes break the rules.  Using this [advice](), modify 
        
        ```
        nano debian.master/config/annotations
        ```
        
        1. search for "CONFIG_KEYBOARD_ATKBD", "CONFIG_SERIO_I8042", and "CONFIG_SERIO_LIBPS2" and set amd64 option to "m" for each.
        
    1. build
    
        ```
        LANG=C fakeroot debian/rules clean
        # if you need linux-tools or lowlatency kernel, run instead:
        LANG=C fakeroot debian/rules binary
        ```

    1. Install the three-package set (on your build system, or on a different target system) with dpkg -i and then reboot:
    
        ```

        sudo dpkg -i linux*5.11.0*.deb
        sudo apt install -f #to install any missing packages
        sudo apt autoremove # to remove any unused packages
        sudo reboot
        ``` 
    



## Other info

* <https://www.mail-archive.com/search?l=ubuntu-bugs@lists.ubuntu.com&q=subject:%22%5C%5BBug+1943832%5C%5D+Re%5C%3A+Keyboard+doesn%27t+work+on+a+%5C%22cold+boot%5C%22+with+built%5C-in+%5C%22i8042+PC+Keyboard+controller%5C%22+%5C%28ASUS+UM425UA%5C%29%22&o=newest&f=1>

