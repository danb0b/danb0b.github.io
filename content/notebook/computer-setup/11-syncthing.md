---
title: Syncthing
weight: 11
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