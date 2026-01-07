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
  valid users = danaukes
```

other useful parameters:

```text
read only = yes
guest ok = no
browsable = yes
valid users = user1 user2
write list = user1
read list = user2
```

```bash
sudo systemctl restart smbd.service 
sudo systemctl restart smbd.service nmbd.service
sudo ufw allow samba
sudo smbpasswd -a <username>
```

Then connect to your new share!

## Step 2: permissions

Make sure you have updated file owner, group, and permissions to reflect the samba settings here.  You might need to ensure that the folder above the shared folder gives the particular user access, as well.

```bash
chown -R username:groupname /path/to/share
chown -R 755 /path/to/share
chown  755 /path/to/
```

## External References

* <https://forums.servethehome.com/index.php?threads/the-skinny-on-windows-11-and-linux-samba-shares.42727/>
* [SAMBA - do not have permission to access....[SOLVED]](https://forums.linuxmint.com/viewtopic.php?t=245005)
