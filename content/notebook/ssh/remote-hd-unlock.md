---
title: Remote Unlock your LUKS-encrypted Hard Drive
tags:
  - ubuntu
  - linux
  - ssh
  - security
weight: 10
---

Updated for Ubuntu 22.04

1. Install Software

    ```bash
    sudo apt update
    sudo apt -y upgrade
    sudo apt install -y busybox dropbear*
    ```

1. Create and add key

    ```bash
    ssh-keygen -b 4096 -t rsa -f ~/luks_unlock_key -N=""
    ```

    then add your public key (most of the time ~/.ssh/id_rsa.pub) in the file /etc/dropbear/initramfs/authorized_keys.
    
    ```bash
    sudo cat ~/lucks_unlock_key.pub >> /etc/dropbear/initramfs/authorized_keys
    ```
    
    or, if you need to do it as root:
    
    ```bash
    sudo -i
    sudo echo "mypublickeydata" >> /etc/dropbear/initramfs/authorized_keys
    exit
    ```

1. Update config (optional)

    ```bash
    sudo nano /etc/dropbear/initramfs/dropbear.conf
    ```
    Add these options: 
    
    * -I - disconnect time
    * -j - disable local ssh port forwarding
    * -k - disable remote ssh port forwarding
    * -p - listen on port 2222
    * -s - disable password logins
    
    ```bash
    #DROPBEAR_OPTIONS="-I 180 –j –k –p 2222 -s"
    DROPBEAR_OPTIONS="-p 2222"
    ```

1. Set Static IP (optional)

    ```
    sudo nano /etc/initramfs-tools/initramfs.conf
    ```
    
    Add config:
    
    ```
    IP:IPADDRESS::GATEWAY:NETMASK:HOSTNAME:ADAPTER
    ```
    
    ```
    IP=192.168.0.100::192.168.0.1:255.255.255.0:ubuntu:enp2s0
    ```

1. Update initramfs

    Update initramfs to take into account the changes: :

    ```bash
    sudo update-initramfs -u -k all
    ```

1. Setup .ssh/config

    if you want to avoid to have clash between the keys between dropbear and openssh (they share the same ip, but use a different key), you may want to put in your client ~/.ssh/config something like that:

    ```
    Host <myserver>_luks_unlock
         User root
         Hostname <myserver-ip-or-hostname>
         # The next line is useful to avoid ssh conflict with IP
         HostKeyAlias <myserver>_luks_unlock
         Port 2222 #use the unlock port defined in the dropbear config above rather than the normal port defined in sshd config
         PreferredAuthentications publickey
         IdentityFile /path/to/id_rsa
    Host <myserver>
         User <normalusername>
         Hostname <myserver-ip-or-hostname>
         Port 22 #use the normal port defined in sshd config
         PreferredAuthentications publickey
         IdentityFile /path/to/id_rsa
    ```

1. Connect

    Connect using:

    ```bash
    ssh myserver_luks_unlock
    ```

    and once you get a prompt, type as suggested by the busybox text :

    ```bash
    cryptroot-unlock
    ```

## References

* <https://www.pbworks.net/ubuntu-guide-dropbear-ssh-server-to-unlock-luks-encrypted-pc/>
* <https://unix.stackexchange.com/questions/411945/luks-ssh-unlock-strange-behaviour-invalid-authorized-keys-file>
* <https://unix.stackexchange.com/questions/5017/ssh-to-decrypt-encrypted-lvm-during-headless-server-boot>
* [instructions for using a usb stick](https://gist.github.com/da-n/4c77d09720f3e5989dd0f6de5fe3cbfb)
* [meaning of HostKeyAlias](https://serverfault.com/questions/193631/ssh-into-a-box-with-a-frequently-changed-ip)
