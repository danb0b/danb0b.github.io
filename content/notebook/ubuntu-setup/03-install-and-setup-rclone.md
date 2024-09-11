---
title: 03-Install and Setup ```rclone```
weight: 30
tags:
- ubuntu
- linux
- rclone
summary: how to install and setup rclone
---

1. Install ```rclone```

    ```bash
    sudo apt install -y curl
    curl https://rclone.org/install.sh | sudo bash
    ```

1. If you have a previous config for rclone, it should be encrypted before backing up.  Now you can reload it back to your computer

    ```bash
    mkdir ~/.config
    mkdir ~/.config/rclone
    gpg --output ~/.config/rclone/rclone.conf --decrypt /my/remote/filesystem/backup_settings/rclone.conf.pgp
    ```

1. Create file structure for rclone.  Let's say you have set up a remote filesystem called dropbox_personal.  

    ```bash
    sudo mkdir /media/shared-folder-name
    sudo chown username:groupname /media/shared-folder-name
    ```

    and repeat for any other cloud folders you have set up in config

    for example:

    ```bash
    sudo mkdir /media/dropbox_personal
    sudo chown danaukes:danaukes /media/dropbox_personal
    
    sudo mkdir /media/dropbox_asu
    sudo chown danaukes:danaukes /media/dropbox_asu
    
    sudo mkdir /media/drive_asu
    sudo chown danaukes:danaukes /media/drive_asu
    
    sudo mkdir /media/onedrive-idealab
    sudo chown danaukes:danaukes /media/onedrive-idealab
    ```

1. Mount

    ```bash
    rclone mount <rclone_id>: /media/<shared-folder-name> --vfs-cache-mode full &
    ```

    repeat for any other cloud folders you have set up in config.

    for example:

    ```bash
    rclone mount onedrive-idealab: /media/onedrive-idealab --vfs-cache-mode full &
    rclone mount dropbox_asu: /media/dropbox_asu --vfs-cache-mode full &
    rclone mount asu: /media/drive_asu --vfs-cache-mode full &
    rclone mount dropbox_personal: /media/dropbox_personal --vfs-cache-mode full &
    ```

1. For older distributions fuse3 is not available.  Try:

    ```bash
    sudo ln -s /bin/fusermount /bin/fusermount3
    ```