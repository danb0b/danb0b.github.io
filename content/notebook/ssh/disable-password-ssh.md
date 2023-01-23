---
title: Disabling Password-based SSH
summary: Settings for hardening ssh on Ubuntu
tags:
  - ssh
  - ubuntu
  - linux
  - security
weight: 10
---

first, remember to add a public key to your .ssh/authorized keys so you can still log in remotely.

```
echo "<public key info here>" >> /.ssh/authorized_keys
```

test your current keys:

```bash
sudo sshd -t
```

retrieve your current config

```bash
sudo sshd -T
```

from [here](https://www.sshaudit.com/hardening_guides.html#ubuntu_20_04_lts):

save the original file:

```bash
sudo cp /etc/ssh/moduli /etc/ssh/moduli.old
```

enter root mode

```bash
sudo -i
```

paste in the following to remove small moduli

```bash
awk '$5 >= 3071' /etc/ssh/moduli > /etc/ssh/moduli.safe
mv /etc/ssh/moduli.safe /etc/ssh/moduli
exit
```

Harden your config

Derived from [this link](https://motorscript.com/security-hardening-ssh-linux-server/) and [this link](https://linux-audit.com/audit-and-harden-your-ssh-configuration/)

```
cat <<EOT >> 99-local-sshd.conf
#AllowUsers username1 username2
#Port 23456
IgnoreRhosts yes
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
ChallengeResponseAuthentication no
KerberosAuthentication no
GSSAPIAuthentication no
#UsePAM no
X11Forwarding no
MaxAuthTries 3
LoginGraceTime 20
PermitUserEnvironment no
DebianBanner no

AllowAgentForwarding yes
AllowTcpForwarding no
PermitTunnel no

HostKey /etc/ssh/ssh_host_ed25519_key
HostKey /etc/ssh/ssh_host_rsa_key
#HostKey /etc/ssh/ssh_host_ecdsa_key

# Restrict key exchange, cipher, and MAC algorithms, as per sshaudit.com
# hardening guide.
KexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group-exchange-sha256
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
MACs hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,umac-128-etm@openssh.com
HostKeyAlgorithms ssh-ed25519,ssh-ed25519-cert-v01@openssh.com,sk-ssh-ed25519@openssh.com,sk-ssh-ed25519-cert-v01@openssh.com,rsa-sha2-256,rsa-sha2-512,rsa-sha2-256-cert-v01@openssh.com,rsa-sha2-512-cert-v01@openssh.com

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


