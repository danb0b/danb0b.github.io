---
title: ASUS Zenbook Issues
tags:
  - asus
  - linux
  - ubuntu
weight: 99
---

I have an ASUS Zenbook UM425U, currently working great with Ubuntu 21.04 loaded.  Upon installing Ubuntu 20.04, initially the keyboard worked but other aspects of the computer did not, such as being able to control screen brightness, fan speed, etc.  After the kernel was automatically updated, however, suddently I was unable to use the keyboard, but intermittently.  Each reboot might allow me or not.  To add an additional wrinkle, I had also encrypted my hard drive using LUKS, meaning that if I was traveling or did not have access to an external keyboard, I would be locked out.

## Install a compatible Kernel  

The first thing I did was to manually install a kernel I could at least unlock my computer with.  I followed the instructions [here](https://www.how2shout.com/linux/install-linux-5-8-kernel-on-ubuntu-20-04-lts/) to get the linux 5.8.18 kernel installed.

List all kernels:

```bash
dpkg --list | grep linux-image
```

## Recompile your Kernel

The real solution, however, is discussed in this [chain of emails](https://www.mail-archive.com/search?l=ubuntu-bugs@lists.ubuntu.com&q=subject:%22%5C%5BBug+1943832%5C%5D+Re%5C%3A+Keyboard+doesn%27t+work+on+a+%5C%22cold+boot%5C%22+with+built%5C-in+%5C%22i8042+PC+Keyboard+controller%5C%22+%5C%28ASUS+UM425UA%5C%29%22&o=newest&f=1), and the solution is discussed  [here](https://www.mail-archive.com/ubuntu-bugs@lists.ubuntu.com/msg5955393.html).

1. open ```software-properties-gtk``` and enable source code
1. Follow instructions to [build your own kernel](https://wiki.ubuntu.com/Kernel/BuildYourOwnKernel)

    1. get dependencies
    1. get source ()

        ```bash
        apt source linux-image-unsigned-$(uname -r)
        ```

    1. update configs

        ```bash
        chmod a+x debian/rules
        chmod a+x debian/scripts/*
        chmod a+x debian/scripts/misc/*
        LANG=C fakeroot debian/rules clean
        LANG=C fakeroot debian/rules editconfigs # you need to go through each (Y, Exit, Y, Exit..) or get a complaint about config late
        ```

    1. Use the advice from [here](https://www.mail-archive.com/ubuntu-bugs@lists.ubuntu.com/msg5955393.html), update yoru configuration (don't uncheck "support for uevent")

        ```txt
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

    1. These changes break the rules.  Modify

        ```bash
        nano debian.master/config/annotations
        ```

        1. search for "CONFIG_KEYBOARD_ATKBD", "CONFIG_SERIO_I8042", and "CONFIG_SERIO_LIBPS2" and set amd64 option to "m" for each.

    1. Update version number so that the apt repository doesn't supersede it on the next upgrade (according to [the ubuntu guide](https://wiki.ubuntu.com/Kernel/BuildYourOwnKernel#Modifying_the_configuration))

       * add a local version modifier like "+test1" to the end of the first version number in the debian.master/changelog file before building.
       * This will help identify your kernel when running as it also appears in uname -a.
       * Note that when a new Ubuntu kernel is released that will be newer than your kernel (which needs regenerating), so care is needed when upgrading.
       * **NOTE:** do not attempt to use CONFIG_LOCALVERSION as this _will_ break the build.

       ```bash
       nano debian.master/changelog
       ```

    1. build

        ```bash
        LANG=C fakeroot debian/rules clean
        # quicker build:
        LANG=C fakeroot debian/rules binary-headers binary-generic binary-perarch
        # if you need linux-tools or lowlatency kernel, run instead:
        LANG=C fakeroot debian/rules binary
        ```

    1. Install the three-package set (on your build system, or on a different target system) with dpkg -i and then reboot:

        ```bash
        sudo dpkg -i linux*5.11.0*.deb
        sudo apt install -f #to install any missing packages
        sudo apt autoremove # to remove any unused packages
        sudo reboot
        ```

    1. Reinstall virtualbox-dkms

        ```bash
        sudo apt install --reinstall virtualbox-dkms 
        sudo modprobe vboxdrv
        ```

------

## Things that didn't work

## Modify initramfs

find HID modules

```bash
lsmod
```

add those modules to initramfs

```bash
sudo nano /etc/initramfs-tools/modules
```

add one per line

```bash
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

```bash
sudo update-initramfs -u -k all
```

## Blacklist ```amdgpu```

when doing update-initramfs in kernel 5.11.0-31, there are some messages about amdgpu missing drivers

Add the following line to /etc/modprobe.d/blacklist.conf.

```bash
blacklist amdgpu
```

As initramfs contains modprobe configuration, update the initramfs and reboot:

```bash
sudo update-initramfs -u -k all
```

Check whether the driver blacklisted or not, the following command should output nothing.

```bash
lsmod | grep amdgpu
```

But this kills hdmi...
