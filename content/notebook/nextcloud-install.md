---
title: Nextcloud Installation
tags:
  - ubuntu
  - linux
  - nextcloud
---

1. Prerequisites

    ```
    sudo apt install openssh-server net-tools
    ```

1. Install
    
    ```
    sudo snap install nextcloud
    ```
    
1. Configure

    ```
    sudo nextcloud.manual-install <username> <password>
    ```


    ```
    sudo nextcloud.occ config:system:set trusted_domains 1 --value=<example.com>
    ```

    ```
    sudo nextcloud.occ config:system:set trusted_domains 1 --value=192.168.0.219
    sudo ufw allow 22
    sudo ufw allow 80,443/tcp
    ```



1. certificate
    ```
    sudo nextcloud.enable-https lets-encrypt
    ```
    ```
    sudo nextcloud.enable-https self-signed
    ```
## External References

<https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-nextcloud-on-ubuntu-20-04>