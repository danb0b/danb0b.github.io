---
title: 03-Install and Setup ```rclone```
weight: 30
tags:
- ubuntu
- linux
- rclone
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
    mkdir /media/dropbox_personal
    sudo chown username:groupname /media/dropbox_personal
    #... 
    # repeat for any other cloud folders you have set up in config
    ```

1. Mount

    ```bash
    rclone mount dropbox_personal: /media/dropbox_personal --vfs-cache-mode full &
    #... 
    #repeat for any other cloud folders you have set up in config
    ```
