---
title: Remote Unlock your LVM-encrypted Hard Drive
tags:
  - ubuntu
  - linux
  - ssh
---



1. Install Software

    ```bash
    sudo apt install busybox dropbear*
    ```

1. Create and add Key

    ```bash
    ssh-keygen -b 4096
    ```

    then add your public key (most of the time ~/.ssh/id_rsa.pub) in the file /etc/dropbear-initramfs/authorized_keys.

1. Update initramfs

    Update initramfs to take into account the changes: :

    ```bash
    sudo update-initramfs -u -k all
    ```

1. Setup .ssh/config

    if you want to avoid to have clash between the keys between dropbear and openssh (they share the same ip, but use a different key), you may want to put in your client ~/.ssh/config something like that:

    ```
    Host myserver_luks_unlock
         User root
         Hostname <myserver>
         # The next line is useful to avoid ssh conflict with IP
         HostKeyAlias <myserver>_luks_unlock
         Port 22
         PreferredAuthentications publickey
         IdentityFile ~/.ssh/id_rsa
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

* <https://unix.stackexchange.com/questions/411945/luks-ssh-unlock-strange-behaviour-invalid-authorized-keys-file>
* <https://unix.stackexchange.com/questions/5017/ssh-to-decrypt-encrypted-lvm-during-headless-server-boot>
* [instructions for using a usb stick](https://gist.github.com/da-n/4c77d09720f3e5989dd0f6de5fe3cbfb)

