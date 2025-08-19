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

## Intro

In this day and age, using passwords in SSH is fraught with extra security implications.  Keys are a standardized and secure approach to connecting to other machines, in a way that prevents many of the issues of remembering, using, and storing passwords.  However, if you still enable passwords to be used, you can be sure someone will try.

In order to make SSH accessible, some of the default settings are too permissive.  The following tutorial helps you remove older and less secure connection methods, turn off common but typically unnecessary settings, and disable passwords.

> It should be mentioned that if you follow these steps over a remote connection, you should 1) keep an existing connection to your remote server while you implement these changes, and 2) make sure you have a secondary way to gain access should you mess up a step.

## Steps

First, remember to add your public key to the server's .ssh/authorized keys file, so you can still log in remotely.  Generating a key pair is covered in a previous chapter.  If it is on the same machine you are working with, you can simply copy the text in.

once logged on to the server,

```bash
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

back up your current sshd config.  this consists of any/all files in ```/etc/ssh/sshd_config.d/```.  Then paste in the following (size reduced for pdf)

```bash
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

### Client Side

> You should do this on any/all machines that you intend to connect _to_ your server from, in order to match its new settings

Regenerate your keys

```bash
sudo rm -f /etc/ssh/ssh_host_*key*

sudo ssh-keygen -o -t ed25519 -N '' -f /etc/ssh/ssh_host_ed25519_key
sudo ssh-keygen -o -t rsa -b 4096 -N '' -f /etc/ssh/ssh_host_rsa_key
```

Add this to or create a .ssh/config file, at the bottom (size reduced for pdf):

```text
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

## External Resources

* <https://www.designed-cybersecurity.com/tutorials/harden-openssh-config/>
* <https://github.com/trimstray/the-practical-linux-hardening-guide/wiki/OpenSSH>
* <https://thelinuxcode.com/linux_pam_tutorial/>
* <https://www.cyberciti.biz/tips/linux-unix-bsd-openssh-server-best-practices.html>
* <https://www.sshaudit.com/hardening_guides.html#ubuntu_20_04_lts>
* <https://linuxhandbook.com/ssh-disable-password-authentication/>
* older:
    * <https://motorscript.com/security-hardening-ssh-linux-server/>
    * <https://www.digitalocean.com/community/tutorials/how-to-harden-openssh-on-ubuntu-18-04>
    * <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
