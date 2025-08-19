---
title: Software Management
summary: " "
---




### Introduction

We hope to answer

1. what are repositories
1. what is a package
1. how to install packages
1. how to update your computer
1. other commands (remove, purge, list)
1. other flags(-y, -f, ...)
1. ```dpkg``` vs ```apt``` vs ```apt-get```

## APT / dpkg

find installed packages

```bash
sudo apt list --installed *<part-of-package-name>*
```

look for packages to install, with more info

```bash
apt search <part-of-package-name>
```

or

```bash
dpkg --list | grep <package-name-fragment>
```

reinstall package

```bash
sudo apt --reinstall install <package>
```

Update packages

```bash
sudo apt update && sudo apt upgrade
```

> Note: we want to prevent "unattended" upgrades on hardware.  (only upgrade when we mean to).  upgrading can also block us from installing something we need, or introduce new bugs at a bad time.

```bash
sudo apt remove -y unattended-upgrades
```

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

To list the repositories on your system, you can use the command:

```bash
apt policy
```

### Remove a repository

To remove a repository:

```bash
sudo add-apt-repository --remove ppa:PPA_Name/ppa
```

## Show all manually-installed packages

when you want to install a package, sometimes many other dependencies get installed that you did not specify.  Here's how you can list packages installed intentionally vs required dependences  that were not specified

```bash
apt-mark showmanual
```

## Duplicate Installed Packages

To clone your system to another system. Or make a backup. In a terminal type:

```bash
dpkg --get-selections | grep -v deinstall > ubuntu-files
```

This command makes a file list of all installed packages in your system (and stores it in present working directory). Backup this file in hdd, email, etc...(this file is very small).

In the freshly installed ubuntu system run:

```bash
sudo dpkg --set-selections <./ubuntu-files (will set it up and)
apt -y update
apt dselect-upgrade
```

This will install only those packages you had installed (with apt) in the old system.

                                    (OR)
You could back up all the .deb packages from ```/var/cache/apt/archives/``` and install them manually using:

```bash
dpkg -i *.deb
```

And after that running an update cycle later.

## Identifying packages installed via logs

You can inspect logs to find installed files:

```bash
less /var/log/apt/history.log
```

Older log files have a number suffix and are compressed. So to view the next history log, use:

```bash
zless /var/log/apt/history.log.1.gz
```

To view the logs available:

```bash
ls -la /var/log/apt/
```

Thus, the first step is to  find the first line number where a particular date occurs

```bash
cat /var/log/apt/term.log | grep -n 08-15
```

do that again to find the beginning of the second date range if necessary

```bash
cat /var/log/apt/term.log | grep -n 08-16
```

Then use this technique to select only part of the log and then identify newly added packages

```bash
sed '915,10000000!d' /var/log/apt/term.log | grep -i "selecting previously unselected"
```

this returns something like

```bash
Selecting previously unselected package libglfw3:amd64.
Selecting previously unselected package libgl1-mesa-glx:amd64.
Selecting previously unselected package libosmesa6:amd64.
...
Selecting previously unselected package libosmesa6-dev:amd64.
Selecting previously unselected package libglu1-mesa-dev:amd64.
Selecting previously unselected package libglew-dev:amd64
```

by doing a quick find/replace you can then clean up the list and do a ```sudo apt remove```

```bash
sudo apt remove libglfw3:amd64 libgl1-mesa-glx:amd64 libosmesa6:amd64 \
...
libegl1-mesa-dev:amd64 libosmesa6-dev:amd64 libglu1-mesa-dev:amd64
```

## External References

* <http://askubuntu.com/questions/21657/ddg#21658>
