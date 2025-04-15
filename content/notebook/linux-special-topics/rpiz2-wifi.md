---
title: Setting Raspberry Pi Zero 2 as a Wifi Access Point
---

```bash
sudo apt install network-manager
```

comment out ```networkd``` and use ```NetworkManager```
add ```mode: ap```

```yaml
network:
    version: 2
    wifis:
#        renderer: networkd
        renderer: NetworkManager
        wlan0:
            dhcp4: true
            optional: true
            access-points:
                my_access_point:
                    password: my_password 
                    mode: ap
```
