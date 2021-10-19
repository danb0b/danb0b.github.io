---
title: Disabling Password-based SSH
tags:
  - ssh
  - ubuntu
  - linux
  - security
---

Derived from [this link](https://motorscript.com/security-hardening-ssh-linux-server/)

```
cat <<EOT >> 99-local-sshd.conf
#AllowUsers username1 username2
#Port 23456
PermitRootLogin no
PasswordAuthentication no
ChallengeResponseAuthentication no
UsePAM no
X11Forwarding no
AllowTcpForwarding no

HostKey /etc/ssh/ssh_host_ed25519_key
#HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_ecdsa_key

KexAlgorithms curve25519-sha256@libssh.org,ecdh-sha2-nistp521,ecdh-sha2-nistp384,ecdh-sha2-nistp256,diffie-hellman-group-exchange-sha256
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,umac-128@openssh.com

LogLevel VERBOSE

ClientAliveInterval 300
ClientAliveCountMax 0

EOT

chmod 644 99-local-sshd.conf
sudo cp 99-local-sshd.conf /etc/ssh/sshd_config.d/
sudo /etc/init.d/ssh reload #Reload or restart the ssh server
rm 99-local-sshd.conf
```

## References

* <https://www.digitalocean.com/community/tutorials/how-to-harden-openssh-on-ubuntu-18-04>
* <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>

---

# Old Instructions

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
