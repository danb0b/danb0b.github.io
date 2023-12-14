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
    
## Warning

Hard to backup and manage files because snap data is stored in  root.

Workaround: 

<https://github.com/nextcloud-snap/nextcloud-snap/wiki/Change-data-directory-to-use-another-disk-partition>

## External References

* <https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-nextcloud-on-ubuntu-20-04>
* [syncing](https://docs.nextcloud.com/server/latest/user_manual/en/groupware/sync_android.html)
* [android apps](https://livtec.ch/en/the-10-best-nextcloud-apps-for-your-android-smartphone/)


----------------

```bash
docker compose exec --user www-data app php occ config:system:get  trusted_domains
docker compose exec --user www-data app php occ config:system:get  trusted_domains 0
docker compose exec --user www-data app php occ config:system:set  trusted_domains 4 --value=<hostnameorip>
```


## Docker-Compose info

* <https://help.nextcloud.com/t/nextcloud-docker-compose-how-to-update-domain-name-in-config-php/103522>
* <https://docs.nextcloud.com/server/20/admin_manual/configuration_server/config_sample_php_parameters.html#default-parameters>
* <https://docs.nextcloud.com/server/20/admin_manual/configuration_server/occ_command.html>
* <https://github.com/nextcloud/docker#running-this-image-with-docker-compose>
* <https://hub.docker.com/_/nextcloud>
* <https://help.nextcloud.com/t/nexcloud-deployment-by-docker-compose/90660>
* <https://blog.ssdnodes.com/blog/installing-nextcloud-docker/>

More Recent

* <https://adamtheautomator.com/nextcloud-docker/>
* <https://github.com/nextcloud/docker>
* <https://hub.docker.com/_/nextcloud>

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


## Upgrading Nextcloud on Docker

* <https://help.nextcloud.com/t/whats-the-right-way-to-upgrade-nextcloud-on-docker/139411>
* <https://nubisoft.io/blog/how-to-upgrade-dockerized-nextcloud/>
* <https://philenius.github.io/cloud/2022/11/13/how-to-updade-nextcloud-docker-installation-to-latest-version.html>
* <https://forum.openmediavault.org/index.php?thread/31542-how-to-upgrade-nextcloud-in-docker/>
