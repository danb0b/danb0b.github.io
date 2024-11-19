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

## Harden your config

### Client Side

Regenerate your keys

```bash
sudo rm -f /etc/ssh/ssh_host_*key*

sudo ssh-keygen -o -t ed25519 -N '' -f /etc/ssh/ssh_host_ed25519_key
sudo ssh-keygen -o -t rsa -b 4096 -N '' -f /etc/ssh/ssh_host_rsa_key
```

```bash
Host *
    Protocol 2
    HostKeyAlgorithms sk-ssh-ed25519@openssh.com,ssh-ed25519,rsa-sha2-512,rsa-sha2-256,ssh-rsa
    KexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org,diffie-hellman-group18-sha512,diffie-hellman-group16-sha512
    Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
    MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512,hmac-sha2-256
    StrictHostKeyChecking ask
    VerifyHostKeyDNS ask
    ForwardAgent no
    ForwardX11 no
    ForwardX11Trusted no
    PermitLocalCommand no
    HashKnownHosts yes
    TCPKeepAlive yes
    SendEnv LANG LC_*
```

### Server-Side

create a new group and add

```bash
sudo groupadd --system ssh-users
sudo usermod -a -G ssh-users $USER
```
Regenerate your keys
```bash
sudo rm -f /etc/ssh/ssh_host_*key*

sudo ssh-keygen -o -t ed25519 -N '' -f /etc/ssh/ssh_host_ed25519_key
sudo ssh-keygen -o -t rsa -b 4096 -N '' -f /etc/ssh/ssh_host_rsa_key
```

```bash
NUM=$(ls -1 /etc/ssh/sshd_config.d/99-local-sshd.conf* | wc -l)
sudo cp "/etc/ssh/sshd_config.d/99-local-sshd.conf" "/etc/ssh/sshd_config.d/99-local-sshd.conf.bak.$NUM"
cat << EOT | sudo tee /etc/ssh/sshd_config.d/99-local-sshd.conf
Protocol 2
HostKey /etc/ssh/ssh_host_ed25519_key
HostKey /etc/ssh/ssh_host_rsa_key

HostKeyAlgorithms sk-ssh-ed25519@openssh.com,ssh-ed25519,rsa-sha2-512,rsa-sha2-256,ssh-rsa
PubkeyAcceptedKeyTypes sk-ssh-ed25519@openssh.com,ssh-ed25519,rsa-sha2-512,rsa-sha2-256,ssh-rsa
KexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org,diffie-hellman-group18-sha512,diffie-hellman-group16-sha512
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512,hmac-sha2-256

PermitRootLogin prohibit-password
AllowGroups ssh-users

PubkeyAuthentication yes

ChallengeResponseAuthentication no
PasswordAuthentication no
PermitEmptyPasswords no

HostbasedAuthentication no
IgnoreRhosts yes
EOT
sudo systemctl restart ssh
```

summary: ""
---

## Harden your config (old)

Derived from [this link](https://motorscript.com/security-hardening-ssh-linux-server/) and [this link](https://linux-audit.com/audit-and-harden-your-ssh-configuration/)

```

cat <<EOT | sudo tee  /etc/ssh/sshd_config.d/99-local-sshd.conf

# AllowUsers username1 username2

# Port 23456

IgnoreRhosts yes
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
ChallengeResponseAuthentication no
KerberosAuthentication no
GSSAPIAuthentication no

# UsePAM no

MaxAuthTries 3
LoginGraceTime 20
PermitUserEnvironment no
DebianBanner no

# adjust the following to fit your needs and "threat profile"

X11Forwarding yes
AllowAgentForwarding yes
AllowTcpForwarding yes
PermitTunnel yes

HostKey /etc/ssh/ssh_host_ed25519_key
HostKey /etc/ssh/ssh_host_rsa_key

# HostKey /etc/ssh/ssh_host_ecdsa_key

# Restrict key exchange, cipher, and MAC algorithms, as per sshaudit.com

# hardening guide

KexAlgorithms curve25519-sha256,<curve25519-sha256@libssh.org>,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group-exchange-sha256
Ciphers <chacha20-poly1305@openssh.com>,<aes256-gcm@openssh.com>,<aes128-gcm@openssh.com>,aes256-ctr,aes192-ctr,aes128-ctr
MACs <hmac-sha2-256-etm@openssh.com>,<hmac-sha2-512-etm@openssh.com>,<umac-128-etm@openssh.com>
HostKeyAlgorithms ssh-ed25519,<ssh-ed25519-cert-v01@openssh.com>,<sk-ssh-ed25519@openssh.com>,<sk-ssh-ed25519-cert-v01@openssh.com>,rsa-sha2-256,rsa-sha2-512,<rsa-sha2-256-cert-v01@openssh.com>,<rsa-sha2-512-cert-v01@openssh.com>

LogLevel VERBOSE

ClientAliveInterval 300
ClientAliveCountMax 0

EOT

sudo chmod 644 /etc/ssh/sshd_config.d/99-local-sshd.conf
sudo systemctl restart ssh

```


## References

* <https://motorscript.com/security-hardening-ssh-linux-server/>
* <https://www.digitalocean.com/community/tutorials/how-to-harden-openssh-on-ubuntu-18-04>
* <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
* [SSH Reference](/notebook/ssh-reference)

### New in 2024

* <https://www.designed-cybersecurity.com/tutorials/harden-openssh-config/>
* <https://github.com/trimstray/the-practical-linux-hardening-guide/wiki/OpenSSH>
* <https://thelinuxcode.com/linux_pam_tutorial/>
* <https://www.cyberciti.biz/tips/linux-unix-bsd-openssh-server-best-practices.html>
