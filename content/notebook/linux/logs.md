---
title: Logs and Logging
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
