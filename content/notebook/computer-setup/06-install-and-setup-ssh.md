---
title: Install and Setup SSH
weight: 06
---

## Basic Steps

1. Make a new directory for holding keys

    ```bash
    mkdir ~/keys
    ```

1. Decrypt your current keys

    Either retrieve your keys from remote through nautilus and unencrypt or use command line

    ```bash
    gpg --output ~/keys/folder/key_filename1 --decrypt my/remote/filesystem/ssh/key_filename1.pgp
    ```

1. Copy in your config file:

    ```bash
    mkdir ~/.ssh
    cp my/remote/filesystem/ssh/config ~/.ssh/config
    ```

1. Set folder permissions

    ```bash
    chmod 700 ~/keys
    chmod 600 ~/keys/*
    chmod 644 ~/keys/*.pub
    chmod 700 ~/.ssh
    chmod 600 ~/.ssh/*
    chmod 644 ~/.ssh/*.pub
    ```

## Other Useful commands

See [SSH Reference](/notebook/ssh-reference) for more info