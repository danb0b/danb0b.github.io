---
title: Using Duplicate Images
---

These are the things you need to change on your system when duplicating the same image to devices, especially when on the same network.

## Update Hostname

check your current hostname

```bash
cat /etc/hostname
```


```bash
echo "<my-new-hostname>" | sudo tee /etc/hostname 
```

## remove host keys and regenerate

All the turtlebots will have the same ssh host keys, which can get confusing.  Regenerate them to ensure they are recognized as different machines over ssh.

```bash
sudo rm /etc/ssh/ssh_host*
sudo ssh-keygen -o -t ed25519 -N '' -f /etc/ssh/ssh_host_ed25519_key
sudo ssh-keygen -o -t rsa -b 4096 -N '' -f /etc/ssh/ssh_host_rsa_key
```

Exit ssh and log back in, following the instructions when it errors out.  You will need to paste in something like:

```bash
ssh-keygen -f "/home/myuser/.ssh/known_hosts" -R "10.166.219.XXX"
```

Log on to ssh again.

## regenerate machine ids

```bash
sudo rm -f /etc/machine-id
sudo dbus-uuidgen --ensure=/etc/machine-id
```

## External Resources

* <https://unix.stackexchange.com/questions/402999/is-it-ok-to-change-etc-machine-id>
