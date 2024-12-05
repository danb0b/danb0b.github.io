---
title: Disabling Printer Scanning
tags:
- ubuntu
- linux
- printing
summary: " "
---

<div class="alert alert-primary">
These don't seem to fix my problem currently.  Use with care.
</div>

derived from [here](https://askubuntu.com/questions/345083/how-do-i-disable-automatic-remote-printer-installation)

## Stop the Service

```bash
sudo systemctl status cups-browsed.service 
sudo systemctl stop cups-browsed.service 
sudo systemctl disable cups-browsed.service 
```

## Disable from .conf

this may be slightly older advice. You can edit the configuration file

```bash
In /etc/cups/cups-browsed.conf, set directive:
```

Set the directive

```
BrowseProtocols none
```
