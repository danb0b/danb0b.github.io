---
title: Setting up Wake on Lan
---

## Wake on Lan

### On the waking computer

```bash
sudo apt install -y etherwake ethtool
```

### On the computer you want to wake

```bash
sudo apt install -y ethtool
```

then use it

```bash
#ethtool <your-interfacename>
ethtool eth0
```

look for the WOL option to see if it's available

### To wake

```bash
#sudo etherwake -i <your interface> <other MAC address>
sudo etherwake -i eno1 90:B1:1C:77:31:0F
```

## Create a service

```cat << EOF | sudo tee /etc/systemd/system/wol.service
[Unit]
Description=Enable Wake-up on LAN

[Service]
Type=oneshot
ExecStart=/usr/sbin/ethtool -s <your-interface> wol g

[Install]
WantedBy=basic.target
```

```bash
sudo chmod 644 /etc/systemd/system/wol.service
sudo systemctl enable wol.service
sudo systemctl start wol.service
sudo systemctl status wol.service 
```

## Disable Network Manager

list connections

```bash
nmcli connection show
```

look for the ethernet connection

```bash
nmcli connection show id 'Profile 1' | grep -i wake
```

should look like this:

```
802-3-ethernet.wake-on-lan:             default
802-3-ethernet.wake-on-lan-password:    --
```
```bash
sudo nmcli connection modify 'Profile 1' 802-3-ethernet.wake-on-lan magic
```

## External Resources

* <https://www.cyberciti.biz/tips/linux-send-wake-on-lan-wol-magic-packets.html>
* <https://www.maketecheasier.com/enable-wake-on-lan-ubuntu/>
