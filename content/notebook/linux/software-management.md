---
title: Software Management
---



## APT / dpkg

```
sudo apt list --installed <package-name-start*>
```

```
sudo apt --reinstall install <package>
```

```bash
dpkg --list | grep <package-name-fragment>
```


```bash
sudo apt update
sudo apt upgrade
```

less /var/log/apt/history.log

 These logs gets rotated (every month I guess), old files will be suffixed with a number and compressed. So to view the next history log, use:

zless /var/log/apt/history.log.1.gz

To view the logs available:

ls -la /var/log/apt/

from [here](http://askubuntu.com/questions/21657/ddg#21658)



## Desktop applications

* ends in .desktop
* found in ```/usr/share/applications```

## Desktop icons

* svg and png typically
* found in ```/usr/share/icons```

## search path

.bashrc holds path variables.


## Upgrade Distro

Based on [this link](https://vitux.com/how-to-upgrade-ubuntu-20-04-to-21-04/)

1. Might as well be fully updated first

    ```bash
    sudo apt update
    sudo apt upgrade
    sudo shutdown -r now
    ```

1. edit which upgrade you want to do (lts or normal)

    ```bash
    sudo nano /etc/update-manager/release-upgrades
    ```

    change ```prompt=lts``` to ```prompt=normal```

1. run updater

    ```bash
    do-release-upgrade
    ```

    you may need to indicate what to do with specific config files that get updated.

1. Restart

    ```bash
    sudo shutdown -r now
    ```

## Package Management

### List repositories

```bash
apt policy
```

### Remove a repository

```bash
sudo add-apt-repository --remove ppa:PPA_Name/ppa
```

## Show all manually-installed packages

```bash
apt-mark showmanual
```