---
title: Disabling Password-based SSH
tags:
  - ssh
  - ubuntu
  - linux
  - security
---

## Create a new key

Make sure you have already generated a key.  See [SSH Reference](/notebook/ssh-reference) for more info.

## Disable root login and password based login

If working on a remote computer need to log in into server using newly created user named username:

```bash
ssh username@server-ip-or-hostname-here
```

Edit the /etc/ssh/sshd_config file, enter:

```bash
sudo nano /etc/ssh/sshd_config
```

Find ChallengeResponseAuthentication and set to no:

```bash
ChallengeResponseAuthentication no
```

Next, find PasswordAuthentication set to no too:

```bash
PasswordAuthentication no
```

Search for UsePAM and set to no, too:

```bash
UsePAM no
```

Finally look for PermitRootLogin and set it to no too:

```bash
#PermitRootLogin prohibit-password
PermitRootLogin no
```

Save and close the file. Reload or restart the ssh server on Linux:

```bash
/etc/init.d/ssh reload
```

## References

* <https://www.digitalocean.com/community/tutorials/how-to-harden-openssh-on-ubuntu-18-04>
