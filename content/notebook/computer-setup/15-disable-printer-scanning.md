---
title: Disabling Printer Scanning
---


derived from [here](https://askubuntu.com/questions/345083/how-do-i-disable-automatic-remote-printer-installation)

```bash
sudo systemctl stop cups-browsed.service 
sudo systemctl disable cups-browsed.service 
```
