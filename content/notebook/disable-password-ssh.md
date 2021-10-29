---
title: Disabling Password-based SSH
summary: Settings for hardening ssh on Ubuntu
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
PermitEmptyPasswords no
ChallengeResponseAuthentication no
KerberosAuthentication no
GSSAPIAuthentication no
#UsePAM no
X11Forwarding no
AllowTcpForwarding no
AllowAgentForwarding no
MaxAuthTries 3
LoginGraceTime 20
PermitTunnel no

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

* <https://motorscript.com/security-hardening-ssh-linux-server/>
* <https://www.digitalocean.com/community/tutorials/how-to-harden-openssh-on-ubuntu-18-04>
* <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
* [SSH Reference](/notebook/ssh-reference)


