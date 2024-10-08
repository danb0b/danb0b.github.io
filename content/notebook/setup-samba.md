---
title: Setup Samba from Bash
tags: 
  - linux
  - ubuntu
  - samba
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
```

```bash
sudo systemctl restart smbd.service 
sudo ufw allow samba
sudo smbpasswd -a <username>
```

> Then connect to your new share!


## External References

- [SAMBA - do not have permission to access....[SOLVED]](https://forums.linuxmint.com/viewtopic.php?t=245005)
