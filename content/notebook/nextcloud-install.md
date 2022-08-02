---
title: Nextcloud Installation
tags:
  - ubuntu
  - linux
  - nextcloud
weight: 99
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

1. Set Trusted Domain

    set it to the hostname that your server is at, or the ip it is at

    ```
    sudo nextcloud.occ config:system:set trusted_domains 1 --value=<example.com>
    ```

    ```
    sudo nextcloud.occ config:system:set trusted_domains 1 --value=192.168.0.219
    ```

1. certificate

    open up some ports

    ```
    sudo ufw allow 22
    sudo ufw allow 80,443/tcp
    sudo ufw enable
    ```

    select which encryption method

    ```
    sudo nextcloud.enable-https lets-encrypt
    ```
    ```
    sudo nextcloud.enable-https self-signed
    ```

1. Go to the website, sign on as admin, and continue configuring.
    
## External References

* <https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-nextcloud-on-ubuntu-20-04>
* [syncing](https://docs.nextcloud.com/server/latest/user_manual/en/groupware/sync_android.html)
* [android apps](https://livtec.ch/en/the-10-best-nextcloud-apps-for-your-android-smartphone/)


----------------

# Docker-Compose info

* <https://help.nextcloud.com/t/nextcloud-docker-compose-how-to-update-domain-name-in-config-php/103522>
* <https://docs.nextcloud.com/server/20/admin_manual/configuration_server/config_sample_php_parameters.html#default-parameters>
* <https://docs.nextcloud.com/server/20/admin_manual/configuration_server/occ_command.html>
* <https://github.com/nextcloud/docker#running-this-image-with-docker-compose>
* <https://hub.docker.com/_/nextcloud>
* <https://help.nextcloud.com/t/nexcloud-deployment-by-docker-compose/90660>
* <https://blog.ssdnodes.com/blog/installing-nextcloud-docker/>
* <
* <
* <