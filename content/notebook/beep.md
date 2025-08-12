---
title: Beep!
tags: 
- ubuntu
---

1. Comment out pcspkr line in ```/etc/modprobe.d/blacklist.conf```
1. Add yourself to the input group:

    ```bash
    sudo usermod -aG input $USER
    ```

## External Resources

* <https://askubuntu.com/questions/1289288/beep-not-working-since-upgrade-to-20-04-1-lts>
