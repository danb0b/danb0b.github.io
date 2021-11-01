---
title: Disabling Printer Scanning
---


derived from [here](https://askubuntu.com/questions/345083/how-do-i-disable-automatic-remote-printer-installation)

## Stop the Service

```bash
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
