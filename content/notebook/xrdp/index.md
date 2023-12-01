---
title: RDP to another computer
tags:
- linux
- ubuntu
- rdp
---

Derived from [here](https://linuxconfig.org/ubuntu-22-04-remote-desktop-access-from-windows-10)

```bash
sudo apt update
sudo apt install xrdp
```

```bash
sudo systemctl enable --now xrdp
sudo ufw allow from any to any port 3389 proto tcp
```

```bash
sudo service xrdp enable
sudo service xrdp start
```


1. open remmina

1. enter the remote server name

    {{< figure src="screenshot02.png" caption="" >}}

1. Select the default Xorg

    {{< figure src="screenshot04.png" caption="" >}}

    {{< figure src="screenshot05.png" caption="" >}}

1. Select "Dynamic Resolution Update" icon from the left panel.

    {{< figure src="screenshot01.png" caption="" >}}