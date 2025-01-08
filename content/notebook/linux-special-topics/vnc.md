---
title: Installing and Using VNC
tags:
  - linux
  - ubuntu
  - vnc
  - terminal
  - bash
weight: 99
summary: " "
---

```bash
sudo apt update
sudo apt install -y xfce4 xfce4-goodies tightvncserver
vncserver
vncpasswd

vnc password *****

vncserver -kill :1
mv ~/.vnc/xstartup ~/.vnc/xstartup.bak
nano ~/.vnc/xstartup
```

```bash
#!/bin/bash
xrdb $HOME/.Xresources
startxfce4 &
```

```bash
chmod +x ~/.vnc/xstartup
vncserver -localhost
```

```bash
sudo nano /etc/systemd/system/vncserver@.service
```

```
[Unit]
Description=Start TightVNC server at startup
After=syslog.target network.target

[Service]
Type=forking
User=danaukes
Group=danaukes
WorkingDirectory=/home/danaukes

PIDFile=/home/danaukes/.vnc/%H:%i.pid
ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1280x800 -localhost :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable vncserver@1.service
vncserver -kill :1
sudo systemctl start vncserver@1
sudo systemctl status vncserver@1
```
## Port forward to VNC

```bash
ssh -L 59000:localhost:5901 -C -N <servername>
```

## External Links

* <https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-20-04>
* <https://www.answertopia.com/ubuntu/ubuntu-remote-desktop-access-with-vnc/>
