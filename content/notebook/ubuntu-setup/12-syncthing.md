---
title: 12-Syncthing
weight: 120
tags:
- ubuntu
- linux
- syncthing
summary: " "
---

## Install

1. Add the release PGP keys:

    ```bash
    sudo mkdir -p /etc/apt/keyrings
    sudo curl -L -o /etc/apt/keyrings/syncthing-archive-keyring.gpg https://syncthing.net/release-key.gpg    
    echo "deb [signed-by=/etc/apt/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing stable" | sudo tee /etc/apt/sources.list.d/syncthing.list
    printf "Package: *\nPin: origin apt.syncthing.net\nPin-Priority: 990\n" | sudo tee /etc/apt/preferences.d/syncthing
    sudo apt update && sudo apt install -y syncthing
    systemctl --user enable syncthing.service
    systemctl --user start syncthing.service  
    ```

1. add syncthing to your firewall rules

```bash
sudo ufw allow syncthing
sudo ufw allow syncthing-gui
```

1. Configure it to connect to your other computers

## Optional

You can run ```syncthing``` from bash to continue setup just by typing ```syncthing```

## Service Commands

```bash
systemctl --user edit syncthing.service
systemctl --user enable syncthing.service
systemctl --user start syncthing.service  
systemctl --user status syncthing.service
systemctl --user restart syncthing.service  
systemctl --user stop syncthing.service  
systemctl --user disable syncthing.service  
```

## External Resources

* <https://docs.syncthing.net/users/autostart.html#linux>
* <https://docs.syncthing.net/users/faq.html#how-do-i-reset-the-gui-password>
