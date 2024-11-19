---
title: Set up Dovecot and Postfix
tags: 
  - ubuntu
  - linux
  - smtp
  - imap
  - dovecot
  - postfix
params:
  published: false
summary: ""
---

## External References

* <https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-on-ubuntu-20-04>
* <https://docs.gitlab.com/ee/administration/reply_by_email_postfix_setup.html>
* <https://subatomicsolutions.org/8-freebsd/23-smtp-email-server-with-postfix>
* <https://subatomicsolutions.org/8-freebsd/24-imap-or-pop3-email-server-with-dovecot>
* <https://doc.dovecot.org/configuration_manual/quick_configuration/>
* <https://www.arubacloud.com/tutorial/how-to-configure-a-pop3-imap-mail-server-with-dovecot-on-ubuntu-18-04.aspx>
* <https://github.com/docker-mailserver/docker-mailserver/blob/master/README.md>
* <http://www.freekb.net/Article?id=3747>

## Docker Approach

```bash
sudo docker pull instrumentisto/dovecot
docker run --rm instrumentisto/dovecot doveconf > my-dove-conf.conf
docker run -p 143:143 -v ~/my-dove-conf.conf:/etc/dovecot/dovecot.conf instrumentisto/dovecot
docker run -d -p 143:143 -v ~/my-dove-conf.conf:/etc/dovecot/dovecot.conf instrumentisto/dovecot
```

```bash
sudo docker pull dovecot/dovecot
docker run --rm dovecot/dovecot doveconf > my-dove-conf.conf
docker run -p 143:143 -v ~/my-dove-conf.conf:/etc/dovecot/dovecot.conf dovecot/dovecot
docker run -d -p 143:143 -v ~/my-dove-conf.conf:/etc/dovecot/dovecot.conf dovecot/dovecot

docker run -p 143:143 -v ~/etc_dovecot:/etc/dovecot -v ~/srv_mail:/srv/mail dovecot/dovecot
```
