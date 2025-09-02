---
title: ZFS info
tags:
- ubuntu
- linux
- backup
- restore
- storage
summary: " "
---


## Typical backup process

log into your main zfs server

use this one-liner to get the name of the last snapshot in the list, save as a variable, and echo it back:

```bash
last_snapshot=$(zfs list -t snapshot | tail -1 | awk '{print $1}') && echo $last_snapshot
```

form a new variable for your current snapshot

```bash
new_snapshot="<name-of-your-pool>@$(date +"%Y-%m-%d_%H-%M")"
```

for example:

```bash
new_snapshot="coldstorage/nas@$(date +"%Y-%m-%d_%H-%M")"
```

Then take a snapshot and check that it was taken:

```bash
zfs snapshot $new_snapshot && zfs list -t snapshot
```

on secondary machine, ensure that it has the same snapshot:

```bash
zfs list -t snapshot
```

from the primary machine, send it over using the template:

```bash
zfs send -v -i <last_snapshot> <current-snapshot> | ssh <secondary-machine> zfs recv <pool/data>
```

with literals it would look like

```bash
zfs send -v -i coldstorage/nas@2022-05-27 coldstorage/nas@2023-06-08_10-00 | ssh storage zfs recv storage
```

### Full example

open in a tmux window in case your ssh session dies or window is closed:

```bash
tmux
```

Then

```bash
last_snapshot=$(zfs list -t snapshot | tail -1 | awk '{print $1}')
new_snapshot="coldstorage/nas@$(date +"%Y-%m-%d_%H-%M")"
zfs snapshot $new_snapshot
zfs send -v -i $last_snapshot $new_snapshot | ssh storage zfs recv storage
```

## How to set up ZFS

First install it

```bash
sudo apt install -y zfsutils-linux
sudo fdisk -l
lsblk
lsblk -f
```

### define permissions

add permissions using

```bash
sudo zfs allow -u <username> receive,create,send,hold,share,snapshot,mount <name-of pool>
```

For example,

```bash
sudo zfs allow -u danaukes receive,create,send,hold,share,snapshot,mount storage
sudo zfs allow -u danaukes receive,create,send,hold,share,snapshot,mount coldstorage
sudo zfs allow -u danaukes receive,create,send,hold,share,snapshot,mount coldstorage/nas
```

### create a pool

```bash
sudo zpool create -f storage mirror /dev/sdb /dev/sdc
sudo zpool create -f coldstorage mirror /dev/sda /dev/sde
sudo zpool create -f coldstorage mirror /dev/sda /dev/sdb
```

Other useful commands related to pools

```bash
zpool status
zpool status -v
zpool list
sudo zpool destroy <pool-name>
```

Some examples

```bash
sudo zpool mount coldstorage
sudo zpool unmount coldstorage
sudo zpool online coldstorage
sudo zpool offline coldstorage
sudo zpool detatch coldstarge /dev/sdb1
sudo zpool replace -f coldstorage 11380073923137715223 /dev/sdb
```

### import / export

You can import and export an existing pool if it is not currently loaded on your system.

```bash
sudo zpool export coldstorage
sudo zpool import coldstorage -d /dev/
```

## filesystems

<https://docs.oracle.com/cd/E19253-01/819-5461/gfkco/index.html>

```bash
sudo zfs create coldstorage/nas
zfs set readonly=on coldstorage/nas
zfs get mountpoint coldstorage/nas
zfs list
```

rollback snapshots:

```bash
sudo zfs rollback <pool>/<datastore>@<identifier>
sudo zfs rollback coldstorage/nas@test
```

on colorado

```bash
sudo zpool create -f coldstorage mirror /dev/sda /dev/sdb
sudo zfs create coldstorage/nas
sudo zfs set readonly=on coldstorage/nas
sudo zfs rollback coldstorage/nas@test
```

## List all data

```bash
zfs list
zfs list -t filesystem
zfs list -t snapshot
```

## snapshots

```bash
tmux
zfs snapshot <pool>@<data>/<identifier>

zfs snapshot "storage@$(date +"%Y-%m-%d_%H-%M")"

zfs send -v -i <last_snapshot> <current-snapshot> | ssh <secondary-machine> zfs recv <pool/data>
zfs send -v -i storage@2022-05-27 storage@2023-06-08_10-00 | ssh colorado zfs recv coldstorage/nas
```

## Sending recursive snapshots to another locally

```bash
zfs send -R -v storage@test | zfs recv -F coldstorage/nas
```

## Sending recursive snapshots to another datastore remotely

```bash
zfs send -R -v storage@test | ssh colorado zfs recv -F coldstorage/nas
```

## debugging

```bash
sudo dmesg | grep -i zfs
```

## Highlighted External Links

[Managing ZFS File Systems - ZFS Administration Guide](https://illumos.org/books/zfs-admin/gavwq.html#gazvb)

### Other External links

* Main sources:

    * <https://illumos.org/books/zfs-admin/>
    * <https://blog.victormendonca.com/2020/11/03/zfs-for-dummies/>
    * <https://www.willhaley.com/blog/zfs-cheat-sheet/>

* Specific Issues:
    * [can I zfs send to a zfs pool of a different size? - Google Search](https://www.google.com/search?client=firefox-b-1-d&q=can+I+zfs+send+to+a+zfs+pool+of+a+different+size%3F)
    * [replication - how to one-way mirror an entire zfs pool to another zfs pool - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/263677/how-to-one-way-mirror-an-entire-zfs-pool-to-another-zfs-pool)
    * [How to zfs send to another computer ssh - Google Search](https://www.google.com/search?q=How+to+zfs+send+to+another+computer+ssh&client=firefox-b-1-d&ei=pqdrZJ2eLpL9kPIP38u4kA4&ved=0ahUKEwidiaH3uon_AhWSPkQIHd8lDuIQ4dUDCBA&uact=5&oq=How+to+zfs+send+to+another+computer+ssh&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCCEQoAE6CggAEEcQ1gQQsAM6CAgAEIoFEJECOgUIABCABDoLCC4QgAQQsQMQ1AI6CAgAEIAEELEDOgYIABAWEB46CAgAEBYQHhAPOggIABCKBRCGAzoFCCEQqwI6CAghEBYQHhAdOgcIIRCgARAKSgQIQRgAUMYhWOFbYOtcaARwAXgAgAGRAYgBuh6SAQUxMS4yNZgBAKABAcgBCMABAQ&sclient=gws-wiz-serp)
    * [server - Send ZFS snapshot to remote machine - Ask Ubuntu](https://askubuntu.com/questions/764416/send-zfs-snapshot-to-remote-machine)
    * [Sending a ZFS Snapshot - Managing ZFS File Systems in Oracle® Solaris 11.2](https://docs.oracle.com/cd/E36784_01/html/E36835/gbinw.html#scrolltoc)
    * [zfs requires root privileges zvs send ubuntu - Google Search](https://www.google.com/search?client=firefox-b-1-d&q=zfs+requires+root+privileges+zvs+send+ubuntu)
    * [ZFS send/receive over ssh on linux without allowing root login - Super User](https://superuser.com/questions/877186/zfs-send-receive-over-ssh-on-linux-without-allowing-root-login)
    * [docs.oracle.com/cd/E19253-01/819-5461/gfkco/index.html](https://docs.oracle.com/cd/E19253-01/819-5461/gfkco/index.html)
    * [Install and Setup SSH \| Dan Aukes](https://danaukes.com/notebook/ubuntu-setup/07-install-and-setup-ssh/)
    * [docs.oracle.com/cd/E19253-01/819-5461/gbiqe/index.html](https://docs.oracle.com/cd/E19253-01/819-5461/gbiqe/index.html)
    * [ssh pipe zfs send Could not resolve hostname send: Temporary failure in name resolution cannot receive - Google Search](https://www.google.com/search?q=ssh+pipe+zfs+send+Could+not+resolve+hostname+send%3A+Temporary+failure+in+name+resolution+cannot+receive&client=firefox-b-1-d&ei=57FrZKmSCJ7GkPIPg8-b2AM&ved=0ahUKEwjpodTaxIn_AhUeI0QIHYPnBjsQ4dUDCBA&uact=5&oq=ssh+pipe+zfs+send+Could+not+resolve+hostname+send%3A+Temporary+failure+in+name+resolution+cannot+receive&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAFAAWABgAGgAcAF4AIABAIgBAJIBAJgBAKABAQ&sclient=gws-wiz-serp)
    * [ssh: Could not resolve hostname server: Name or service not known - Ask Ubuntu](https://askubuntu.com/questions/874724/ssh-could-not-resolve-hostname-server-name-or-service-not-known)
    * [zfs send \| zfs receive as non-root -- Dan Langille\'s Other Diary](https://dan.langille.org/2015/02/16/zfs-send-zfs-receive-as-non-root/)
    * [cannot hold: permission denied cannot send \'storage\': permission denied cannot receive: failed to read from stream - Google Search](https://www.google.com/search?client=firefox-b-1-d&q=cannot+hold%3A+permission+denied+cannot+send+%27storage%27%3A+permission+denied+cannot+receive%3A+failed+to+read+from+stream+)
    * [Initial Replication Task from On-site Data \| TrueNAS Community](https://www.truenas.com/community/threads/initial-replication-task-from-on-site-data.105983/)
    * [can I change pool size zfs - Google Search](https://www.google.com/search?client=firefox-b-1-d&q=can+I+change+pool+size+zfs)
    * [zfs if I receive a snapshot from a pool of a different size is it resized? - Google Search](https://www.google.com/search?q=zfs+if+I+receive+a+snapshot+from+a+pool+of+a+different+size+is+it+resized%3F&client=firefox-b-1-d&ei=cLRrZPDlKubNkPIPz62MsAk&ved=0ahUKEwjw3bKQx4n_AhXmJkQIHc8WA5YQ4dUDCBA&uact=5&oq=zfs+if+I+receive+a+snapshot+from+a+pool+of+a+different+size+is+it+resized%3F&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAFAAWABgAGgAcAF4AIABAIgBAJIBAJgBAKABAQ&sclient=gws-wiz-serp)
    * [Disabling Password-based SSH \| Dan Aukes](https://danaukes.com/notebook/ssh/disable-password-ssh/)
    * [Monitoring the Progress of ZFS Send Streams - Managing ZFS File Systems in Oracle® Solaris 11.2](https://docs.oracle.com/cd/E36784_01/html/E36835/gnheq.html)
    * [ZFS Send Receive Interrupted \| TrueNAS Community](https://www.truenas.com/community/threads/zfs-send-receive-interrupted.70183/)
    * [Renaming a ZFS pool \-- Prefetch Technologies](https://prefetch.net/blog/2006/11/15/renaming-a-zfs-pool/)
    * [delete zfs pool - Google Search](https://www.google.com/search?q=delete+zfs+pool&client=firefox-b-1-d&ei=5LdrZP7aEaP5kPIP7fGoiAg&ved=0ahUKEwj-3Ny1yon_AhWjPEQIHe04CoEQ4dUDCBA&uact=5&oq=delete+zfs+pool&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoICAAQigUQkQI6EQguEIAEELEDEIMBEMcBENEDOgsIABCABBCxAxCDAToLCC4QigUQsQMQgwE6CwguEIAEEMcBENEDOgoILhCKBRDUAhBDOg4ILhCKBRDHARCvARCRAjoHCC4QigUQQzoHCAAQigUQQzoNCC4QigUQxwEQrwEQQzoRCC4QgwEQxwEQsQMQ0QMQgAQ6CwguEIAEELEDEIMBOhgILhCKBRDUAhBDEJcFENwEEN4EEOAEGAE6CAgAEIAEELEDOgoILhCKBRCxAxBDOggIABAWEB4QD0oECEEYAFDnK1i1QGD5QWgCcAF4AIABzgGIAZ0OkgEFNS45LjGYAQCgAQGwAQDAAQHaAQYIARABGBQ&sclient=gws-wiz-serp)
    * [google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj-3Ny1yon_AhWjPEQIHe04CoEQFnoECAwQAQ&url=https%3A%2F%2Fdocs.oracle.com%2Fcd%2FE19253-01%2F819-5461%2Fgaynd%2Findex.html&usg=AOvVaw0EMZouvqzDhl9WiUIZrUng](https://docs.oracle.com/cd/E19253-01/819-5461/gaynd/index.html)
    * [How to Mount ZFS Filesystems in Different Directories](https://linuxhint.com/mount-zfs-filesystems-in-different-directoris/)
    * [when I zfs send -R does that resize the destination pool? - Google Search](https://www.google.com/search?client=firefox-b-1-d&q=when+I+zfs+send+-R+does+that+resize+the+destination+pool%3F)
    * [SOLVED - Manual zfs replication issue \| TrueNAS Community](https://www.truenas.com/community/threads/manual-zfs-replication-issue.87812/)
    * [file-level backup vs zfs - Google Search](https://www.google.com/search?q=file-level+backup+vs+zfs&client=firefox-b-1-d&ei=Gr1rZJe2G7f8kPIPwpKUoAE&ved=0ahUKEwiXq_Oxz4n_AhU3PkQIHUIJBRQQ4dUDCBA&uact=5&oq=file-level+backup+vs+zfs&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCCEQoAEyBQghEKABOgoIABBHENYEELADOgYIABAHEB46BQgAEIAEOgQIABAeOgYIABAWEB46CAgAEBYQHhAPOggIABCKBRCGAzoICCEQFhAeEB1KBAhBGABQjxRYxC9g-jNoAnABeACAAcYBiAGAC5IBAzMuOZgBAKABAcgBCMABAQ&sclient=gws-wiz-serp)
    * [ZFS vs Borg for incremental backup of media files to cold storage? : r/zfs](https://www.reddit.com/r/zfs/comments/z8b87o/zfs_vs_borg_for_incremental_backup_of_media_files/)
    * [ZFS File System (Introduction) - ZFS Administration Guide](https://illumos.org/books/zfs-admin/zfsover-1.html#gbcpt)
    * [list all datasets zfs - Google Search](https://www.google.com/search?client=firefox-b-1-d&q=list+all+datasets+zfs)
    * [change files in a root pool to a dataset zfs - Google Search](https://www.google.com/search?q=change+files+in+a+root+pool+to+a+dataset+zfs&client=firefox-b-1-d&ei=3cFrZN6ON_zdkPIP8KO-2AQ&ved=0ahUKEwie8bD304n_AhX8LkQIHfCRD0sQ4dUDCBA&uact=5&oq=change+files+in+a+root+pool+to+a+dataset+zfs&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCCEQoAEyBQghEKABMgUIIRCgATIFCCEQoAEyBQghEKABOgoIABBHENYEELADOggIABCKBRCRAjoTCC4QigUQsQMQgwEQxwEQ0QMQQzoRCC4QgAQQsQMQgwEQxwEQ0QM6CwguEIoFELEDEIMBOgsIABCABBCxAxCDAToRCC4QgwEQxwEQsQMQ0QMQgAQ6CAgAEIAEELEDOgsIABCKBRCxAxCDAToOCC4QgAQQsQMQxwEQ0QM6BQgAEIAEOgoIABCKBRCxAxBDOhMILhCDARDHARCxAxDRAxCKBRBDOg0ILhCKBRCxAxDUAhBDOgcIABCKBRBDOggIABCABBDJAzoICAAQigUQkgM6BQguEIAEOggILhCABBCxAzoLCC4QgAQQxwEQrwE6CwguEIAEELEDENQCOgYIABAWEB46CAgAEBYQHhAPOgUIIRCrAjoICCEQFhAeEB06CAgAEIoFEIYDOgoIIRAWEB4QDxAdOgUIABCiBEoECEEYAFDGMVjqX2CqYGgDcAF4AIABrgGIAbsmkgEFMTMuMzCYAQCgAQHIAQjAAQE&sclient=gws-wiz-serp)
    * [zfs rename/move root filesystem into child - Server Fault](https://serverfault.com/questions/440632/zfs-rename-move-root-filesystem-into-child)
    * [PIC18F47Q10 Curiosity Nano Hardware User Guide - PIC18F47Q10-Curiosity-Nano-Hardware-User-Guide-40002103B.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/PIC18F47Q10-Curiosity-Nano-Hardware-User-Guide-40002103B.pdf)
    * [cannot receive new filesystem stream: permission denied - Google Search](https://www.google.com/search?client=firefox-b-1-d&q=cannot+receive+new+filesystem+stream%3A+permission+denied)
    * [ZFS send / receive non-root account \| by Vignesh A Sathiyanantham \| Medium](https://asvignesh.medium.com/zfs-send-receive-non-root-account-1978c284f8e2)
    * Missing Pool:
        * <https://docs.oracle.com/cd/E19253-01/819-5461/gaynp/index.html>
        * <https://www.reddit.com/r/zfs/comments/uxp4wc/zfs_pool_missing_no_pools_available_disk_is/>
        * <https://www.reddit.com/r/zfs/comments/j62lme/zfs_pool_disappeared_after_reboot/>
        * <https://forums.freebsd.org/threads/zfs-pool-missing-after-crash.65206/>
        * <https://www.google.com/search?client=firefox-b-1-d&q=no+pools+available>
        * <https://discuss.linuxcontainers.org/t/zfs-pool-has-disappeared-visible-with-zpool-import-but-not-in-zpool-list/12928/2>
        * <https://www.osso.nl/blog/zpool-import-no-pools-stale-zdb-labels/>
        * <https://www.truenas.com/community/threads/zpool-status-no-pools-available.18122/>
