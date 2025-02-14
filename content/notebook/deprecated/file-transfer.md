---
title: fixing file transfer bug in nautilus
weight: 99
tags: 
  - ubuntu
  - linux
  - bash
  - nautilus
  - file-transfer
summary: " "
---

Issue: Nautilus hangs when I try to copy large files to a NAS.


```bash
sudo echo $((16*1024*1024)) | sudo tee /proc/sys/vm/dirty_background_bytes && \
  sudo echo $((16*1024*1024)) | sudo tee /proc/sys/vm/dirty_bytes
```

```bash
echo '#!/usr/bin/bash' > ~/test.bash
echo "echo \$((16*1024*1024)) | sudo tee /proc/sys/vm/dirty_background_bytes
echo \$((16*1024*1024)) | sudo tee /proc/sys/vm/dirty_bytes" >> ~/test.bash
chmod +x ~/test.bash
```

type ```crontab -e``` and paste in the following:

```
@reboot ~/test.bash
```

## External references

* <https://blog.programster.org/fix-freezes-when-transferring-files>
* <https://www.raspberrypi.org/forums/viewtopic.php?t=215262>

