---
title: 02-Import Keys
weight: 20
tags:
- ubuntu
- linux
- ssh
- gpg
- keys
summary: " "
---

## Install and Setup

1. Install gnupg, nautilus integration (seahorse), and restart nautilus

    ```bash
    sudo apt install -y gnupg
    # sudo apt install -y seahorse seahorse-nautilus # no longer available for gnome file manager/nautilus
    #killall nautilus
    ```


1. Import Keys

    Configuration files can include sensitive information such as passwords, contact information, or other personal information you don't wish to share, even though you may wish to store it in the cloud for easy retrieval.  In that case it's a good idea to encrypt those files with a personal key.  Here is how you load your previously generated key so you can unencrypt them.

    ```bash
    gpg --import "my/remote/filesystem/keys/file.asc"
    ```

1. Install kleopatra

    apt install -y kleopatra

## Other Helpful Key stuff

See [GPG Reference](/notebook/gpg-reference)