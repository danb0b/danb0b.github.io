---
title: Remote Unlock your LVM-encrypted Hard Drive
tags:
  - ubuntu
  - linux
  - ssh
---

```bash
sudo apt install busybox dropbear*
```

then add your public key (most of the time ~/.ssh/id_rsa.pub) in the file /etc/dropbear-initramfs/authorized_keys.

Update then initramfs to take into account the changes: :

```bash
update-initramfs -u
```

That's all!

Note, if you want to avoid to have clash between the keys between dropbear and openssh (they share the same ip, but use a different key), you may want to put in your client ~/.ssh/config something like that:

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

Then, you just connect using:

```bash
ssh myserver_luks_unlock
```

and once you get a prompt, type as suggested by the busybox text :

```bash
cryptroot-unlock
```
