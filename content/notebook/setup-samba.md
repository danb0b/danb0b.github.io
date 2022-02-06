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
sudo apt install samba
sudo nano /etc/samba/smb.conf
```

```
# Adrian's share
[happy]
  comment = Welcome to Happyland
  path = ~/happy
  read only = no
  guest ok = no
  browsable = yes
```

```bash
sudo /etc/init.d/smbd restart
sudo ufw allow samba
sudo smbpasswd -a <username>
```

## Then connect to your new share!
