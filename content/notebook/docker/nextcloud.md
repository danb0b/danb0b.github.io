---
title: Nextcloud in Docker
tags: 
- nextcloud
- docker
- ubuntu
---

## docker-compose

```yaml
version: '2'

volumes:
  nextcloud:
  db:

services:
  db:
    image: mariadb:10.5
    restart: always
    command: --transaction-isolation=READ-COMMITTED --binlog-format=ROW
    volumes:
      - ./db:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=<password1>
      - MYSQL_PASSWORD=<password1>
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud

  app:
    image: nextcloud
    restart: always
    ports:
      - 8080:80
    links:
      - db
    volumes:
      - ./nextcloud:/var/www/html
    environment:
      - MYSQL_PASSWORD=<password1>
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_HOST=db
      - NEXTCLOUD_ADMIN_PASSWORD=<password2>
      - NEXTCLOUD_ADMIN_USER=admin
      - NEXTCLOUD_TRUSTED_DOMAINS=localhost <ip_address1> <ip_address2> <hostname1> <hostname2>

```

## Commands

How to add, query, or set new trusted domains

```bash
docker compose exec --user www-data app php occ config:system:get  trusted_domains
docker compose exec --user www-data app php occ config:system:get  trusted_domains 0
docker compose exec --user www-data app php occ config:system:set  trusted_domains 4 --value=<hostnameorip>
```

## External Resources 

### Docker-Compose info

* <https://help.nextcloud.com/t/nextcloud-docker-compose-how-to-update-domain-name-in-config-php/103522>
* <https://docs.nextcloud.com/server/20/admin_manual/configuration_server/config_sample_php_parameters.html#default-parameters>
* <https://docs.nextcloud.com/server/20/admin_manual/configuration_server/occ_command.html>
* <https://github.com/nextcloud/docker#running-this-image-with-docker-compose>
* <https://hub.docker.com/_/nextcloud>
* <https://help.nextcloud.com/t/nexcloud-deployment-by-docker-compose/90660>
* <https://blog.ssdnodes.com/blog/installing-nextcloud-docker/>
* <https://adamtheautomator.com/nextcloud-docker/>
* <https://github.com/nextcloud/docker>
* <https://hub.docker.com/_/nextcloud>


### Upgrading Nextcloud on Docker

* <https://help.nextcloud.com/t/whats-the-right-way-to-upgrade-nextcloud-on-docker/139411>
* <https://nubisoft.io/blog/how-to-upgrade-dockerized-nextcloud/>
* <https://philenius.github.io/cloud/2022/11/13/how-to-updade-nextcloud-docker-installation-to-latest-version.html>
* <https://forum.openmediavault.org/index.php?thread/31542-how-to-upgrade-nextcloud-in-docker/>

## SSL resources

- <https://help.nextcloud.com/t/ssl-certificate-on-docker-nextcloud-server/117815>
- <https://tailscale.com/blog/docker-tailscale-guide>
- <https://duckduckgo.com/?t=ffab&q=nextcloud+docker+certificate&ia=web>
- <https://help.nextcloud.com/t/howto-running-nextcloud-over-self-signed-https-ssl-tls-in-docker/101973>
- <https://duckduckgo.com/?t=ffab&q=docker+nextcloud+image+for+ssl&ia=web>
- <https://github.com/docker-library/docs/blob/master/nextcloud/README.md>
- <https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/reverse_proxy_configuration.html>
- <https://github.com/nextcloud/docker/blob/master/.examples/docker-compose/with-nginx-proxy/mariadb/apache/docker-compose.yml>