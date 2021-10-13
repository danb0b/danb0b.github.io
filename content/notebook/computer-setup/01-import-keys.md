---
title: Import Keys
weight: 1
---

## Install and Setup

1. Install gnupg, nautilus integration (seahorse), and restart nautilus

    ```bash
    sudo apt install -y gnupg
    sudo apt install -y seahorse seahorse-nautilus
    killall nautilus
    ```

1. Import Keys

    Configuration files can include sensitive information such as passwords, contact information, or other personal information you don't wish to share, even though you may wish to store it in the cloud for easy retrieval.  In that case it's a good idea to encrypt those files with a personal key.  Here is how you load your previously generated key so you can unencrypt them.

    ```bash
    gpg --import "my/remote/filesystem/keys/file.asc"
    ```

## Other Helpful Key stuff

### List gpg keys

```bash
gpg --list-keys
gpg --list-secret-keys
```
prints out ids

### delete gpg secret keys

```bash
gpg --delete-secret-keys KEYIDFROMABOVE
gpg --delete-keys KEYIDFROMABOVE
```
