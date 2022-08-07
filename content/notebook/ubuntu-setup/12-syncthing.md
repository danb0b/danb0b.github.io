---
title: 12-Syncthing
weight: 120
tags:
- ubuntu
- linux
- syncthing
---

## Install

1. Add the release PGP keys:

    ```bash
    sudo curl -s -o /usr/share/keyrings/syncthing-archive-keyring.gpg https://syncthing.net/release-key.gpg
    ```

1. Add the "stable" channel to your APT sources:

    ```bash
    echo "deb [signed-by=/usr/share/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing stable" | sudo tee /etc/apt/sources.list.d/syncthing.list
    ```

1. Increase preference of Syncthing's packages ("pinning")

    ```bash
    printf "Package: *\nPin: origin apt.syncthing.net\nPin-Priority: 990\n" | sudo tee /etc/apt/preferences.d/syncthing
    sudo apt-get update
    sudo apt-get install syncthing
    ```
    
1. run ```syncthing``` from bash to continue setup
1. Once it is set up the way you want, enable it as a user service, as according to the [documentation](https://docs.syncthing.net/users/autostart.html#linux):

    Edit using:

    ```bash
    systemctl --user edit syncthing.service
    ```

    ```bash
    systemctl --user enable syncthing.service
    systemctl --user start syncthing.service  
    ```
    
    Check the status using:
    
    ```bash
    systemctl --user status syncthing.service
    ```

    stop and disable using:

    ```bash
    systemctl --user stop syncthing.service  
    systemctl --user disable syncthing.service  
    ```
    
1. Configure it to connect to your other computers