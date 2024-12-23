---
title: Logging in Ubuntu
summary: A place to hold information about setting up, viewing, and controlling logging.
weight: 99
tags: 
  - linux
  - ubuntu
  - security
---


## Boot Information

more info [here](https://askubuntu.com/questions/995711/where-can-i-find-the-boot-log)

```bash
journalctl --list-boots 
```

Will list all recent boots

```bash
journalctl --boot=<boot id>
```

To just get information about the most recent boot, use

```bash
journalctl -b
```
## External Links

* <https://logtail.com/tutorials/how-to-view-and-configure-linux-logs-on-ubuntu-20-04/>
* <https://ubuntu.com/tutorials/viewing-and-monitoring-log-files#1-overview>