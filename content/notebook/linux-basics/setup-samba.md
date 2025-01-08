---
title: Setup Samba from Bash
tags: 
  - linux
  - ubuntu
  - samba
summary: " "
---

## Make your folder

```bash
mkdir ~/happy
chmod 0700 ~/happy
```

## Set up samba

```bash
sudo apt install -y samba
sudo nano /etc/samba/smb.conf
```

```
# Networked Attached Storage Share
[nas]
  comment = welcome to NAS
  path = /storage/nas
  read only = no
  guest ok = no
  browsable = yes
  ## valid users = danaukes
```

```bash
sudo systemctl restart smbd.service 
sudo systemctl restart smbd.service nmbd.service
sudo ufw allow samba
sudo smbpasswd -a <username>
```

Then connect to your new share!

> Note: Make sure you have updated file owner, group, and permissions to reflect the samba settings here.  You might need to ensure that the folder above the shared folder gives the particular user access, as well.

## External References

* <https://forums.servethehome.com/index.php?threads/the-skinny-on-windows-11-and-linux-samba-shares.42727/>
* [SAMBA - do not have permission to access....[SOLVED]](https://forums.linuxmint.com/viewtopic.php?t=245005)
