---
---

# Create ssh key

ssh-keygen -t ed25519

print public key:

cat .ssh/id_ed25519.pub

add your key(s) to authorized keys:

sudo nano .ssh/authorized_keys

# Disable root login and password based login

We need to log in into server using newly created user named vivek:
ssh vivek@server-ip-here
ssh vivek@server1.cyberciti.biz

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
'''

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
