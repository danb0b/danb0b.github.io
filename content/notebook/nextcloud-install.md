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
    sudo apt install -y openssh-server net-tools
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
    
## Warning

Hard to backup and manage files because snap data is stored in  root.

Workaround: 

<https://github.com/nextcloud-snap/nextcloud-snap/wiki/Change-data-directory-to-use-another-disk-partition>

## External References

* <https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-nextcloud-on-ubuntu-20-04>
* [syncing](https://docs.nextcloud.com/server/latest/user_manual/en/groupware/sync_android.html)
* [android apps](https://livtec.ch/en/the-10-best-nextcloud-apps-for-your-android-smartphone/)



## Nextcloud Integration

### With Thunderbird

* <https://docs.nextcloud.com/server/19/user_manual/pim/sync_thunderbird.html>
* <https://addons.thunderbird.net/en-US/thunderbird/addon/dav-4-tbsync/?src=search>
* <https://addons.thunderbird.net/en-US/thunderbird/addon/tbsync/?src=search>
* <https://github.com/jobisoft/DAV-4-TbSync/>
* <https://github.com/jobisoft/TbSync>

## Google Calendar

* <https://www.lifewire.com/how-to-sync-google-calendar-with-thunderbird-4691009>
* <https://addons.thunderbird.net/en-US/thunderbird/addon/provider-for-google-calendar/?src=search>

