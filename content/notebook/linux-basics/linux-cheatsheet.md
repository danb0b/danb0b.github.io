---
title: Linux / Bash Cheatsheet
tags:
  - linux
  - bash
  - ubuntu
weight: 1
summary: Collected commands, tips, and tricks for working headless in Ubuntu
---

> Note: A lot of these commands are unique and special to Debian or Ubuntu distributions.  There are typically alternate forms of these expressions for other distributions.

## Find Kernel version

```bash
uname -r
```

More detailed information

```bash
uname -a
```

## Find release name

```bash
lsb_release -a
```

List all kernel images installed:

```bash
dpkg --list | grep linux-image
```

## Crontab

how to run python scripts: <https://www.geeksforgeeks.org/how-to-schedule-python-scripts-as-cron-jobs-with-crontab/>

create a new python script

```python
#!/usr/bin/env python3
import time
import os
with open(os.path.expanduser('~/crontest.txt'),'a') as f:
    f.write(time.ctime()+'\n')
```

```bash
chmod +x test.py
```

```bash
crontab -e
```

```bash
# m h  dom mon dow   command
* * * * * $HOME/test.py
```

## GUI

ctrl-h hides and shows "dot" files in nautilus like ```.config``` or ```.ssh/```

## Login, Logout, Restart

```bash
sudo reboot now
sudo shutdown now
gnome-session-quit
```

## Ubuntu Specific

From <https://fostips.com/lid-close-action-ubuntu-21-04-laptop/>

edit ```/etc/systemd/logind.conf``` to configure power options such as lid closing opening,

```bash
HandleLidSwitch=ignore
HandleLidSwitchExternalPower=ignore
HandleLidSwitchDocked=ignore
```

1. Restart Service

```bash
systemctl restart systemd-logind.service
```

## Backup folders

/bin
/boot
/etc
/home
/lib
/lib64
/opt
/root
/sbin
/usr
/var

<https://askubuntu.com/questions/222326/which-folders-to-include-in-backup>

### How to find .desktop file location for a particular application

For example, if "Image Viewer" is in the name of the icon:

```bash
find / -name '*.desktop' -exec grep -H 'Image Viewer' {} \; 2>/dev/null
```

derived from here: <https://askubuntu.com/questions/1160737/how-to-find-desktop-file-location-for-a-particular-application>:

Some default locations listed here: <https://askubuntu.com/questions/1146307/which-desktop-files-belong-where>:

```
/usr/share/applications/gnome-terminal.desktop
~/.local/share/applications/gnome-terminal.desktop
~/.config/gnome-panel/launchers/gnome-terminal.desktop
~/.gnome/apps/gnome-terminal.desktop
```

## Trash

Files can be stuck in ~/.local/share/Trash/expunged when you delete from Nautilus a folder that belongs to you, but contains files which are belong to another user, and it is tricky for Nautilus to handle this situation correctly. To delete them try to use:

```bash
sudo -i
rm -rv /home/<desired_user_name>/.local/share/Trash/expunged/*
exit
```

## More

see [this page](/bookmarks/linux-cheatsheet-links/) for more links

## Accidentally deleted sudoers

use pkexec to do things you would normally do with sudo, like

pkexec cp /path/to/sudo/backup /etc/sudoers

great advice from here: <https://askubuntu.com/questions/438123/accidentally-deleted-etc-sudoers-file>

## close bash without saving history

```bash
unset HISTFILE && exit
```

or

```bash
history -c && history -w && exit
```

## Systemctl

To find services

```bash
sudo systemctl list-units --type=service
```

To reload the service daemon

```bash
sudo systemctl daemon-reload
```

other common functions:

```bash
sudo systemctl edit <servicename>
sudo systemctl enable <servicename>
sudo systemctl start <servicename>
sudo systemctl status <servicename>
sudo systemctl stop <servicename>
sudo systemctl disable <servicename>
sudo systemctl reload <servicename>
sudo systemctl restart <servicename>
```
