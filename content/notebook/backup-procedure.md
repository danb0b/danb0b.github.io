---
title: Annual Backup Process
tags: 
  - ubuntu
  - linux
  - computer
  - backup
---

## Refresh documents

- Update cv
- Update zotero and backup
- Update idealab website

## check app passwords

<https://myaccount.google.com/apppasswords>

## Online Storage

- Backup onedrive
- Backup google drive
- Backup Dropbox
- Move old "active" idealab project folders to archive
- Sort downloads folder
- Sort "to sort" folders
- sort syncthing folders
- go through starred email
- Archive email
- Download zoom videos

## Courses - General

- backup and zip class folders
- Backup canvas
- Backup slack
- Download grades
- Backup final submissions
- move backup canvas to sandbox
    - unpublish assignments

## Foldable Class

- Copy git repositories from foldable
- Download YouTube videos from foldable
- backup mendeley
- unpublish assignments on foldable website
- download all forum questions

## Deployable Class

- unpublish assignments on foldable-robotics website
- Copy git repositories from foldable
- Download YouTube videos from foldable
- download all forum questions

## Flexible Class

- unpublish assignments on foldable website
- download assignments
- download final grades
- download moodle snapshot
- download all forum questions

## Security

- backup authenticator app config to separate device(s).
- Backup photos
- Find best of last year's photos
- Find best of best photos  
- Arrange this year's photos
- backup password manager

## Home and root folders

- backup .ssh/config
- backup /etc/hosts
- backup .config, especially
- texmf directory
- netplan
- thunderbird config
- mozilla config
- rclone config
- gitman config
- network configs in  /etc/NetworkManager/system-connections/

## Misc

- Backup Sara computers
- back up contacts  
- Organize and sort contacts
- Download past years statements
- check and update scans of important documents
- reset passwords
    - wifi
    - computer
- backup .bashrc
- things to review
    - podcasts
    - thunderbird
    - k9 config
    - docker stuff
    - ssh keys
    - browser bookmarks
    - samba credentials
    - vs code configuation
    - virtualbox images
    - docker data
        - nextcloud
        - gitman
        - photoprism
        - immich
        - home assistant

## ZFS

- take a zfs snapshot
- send to backup computer
- take a zenbook backup
- backup NAS to usb drive

----

## Notes

## Comsol

- Delete Solutions in .mph files: <https://www.youtube.com/watch?v=MgZak4oJ_Ck>

## Ansys

- remove .rst (results) files

discussion: <https://www.researchgate.net/post/What-is-the-use-of-the-extension-files-generated-in-ansys>

## Animations

- remove individual screenshots once the video has been rendered

## Raw files

compress .avi to .mp4

## Things to preserve in Linux
  
- Crontab  
- Netplan  
- .config  
- .thunderbird profile  
- mozilla settings --> find ~/.var -iname "prefs.js"  

/Etc/  

- netplan  
- initramfs-tools/initramf.conf  
- hosts

~/.ssh  
~/.keys  
~/.bashrc  

```bash
#apm list >> atom-packages.txt  
snap list >> snap-packages.txt  
flatpak list >> flat-packages.txt  
apt-mark showmanual >> apt-packages.txt  
conda env export > base.yml 
conda activate pybullet
conda env export > pybullet.yml 
```  

directories  
~/Desktop  
~/Downloads  
~/Documents  
~/Pictures  
~/Videos  
~/adb  
~/prism  
~/Zoom  
~/gPodder  
~/texmf  
~/Virtual Machine VMs  
  