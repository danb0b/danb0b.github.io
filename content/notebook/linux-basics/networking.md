---
title: Networking
tags:
- linux
- networking
summary: " "
---

## Networking

list all current ethernet adapters

```bash
ifconfig
```

to bring a specific network interface up or down

```bash
ifconfig <network interface> down
ifconfig <network interface> up
```

```bash
ip link
# or
ip l
```

```bash
ip addr
#or 
ip a
```

output current wifi name

```bash
sudo apt install -y wireless tools
iwgetid
iwgetid -r # just the name
```

### list all wifis

```bash
iwlist wlan0 scan
```

```bash
sudo apt install -y network-manager
nmcli -f in-use,ssid,bssid,signal,bars  dev wifi
```

list wifis

```bash
nmcli d wifi
```

connect to a specific wifi

```bash
nmcli d wifi connect XX:XX:XX:XX:XX:XX
```

<https://askubuntu.com/questions/833905/how-can-i-connect-to-a-specific-bssid>

### Find services using a port

```bash
sudo lsof -i:3389
```

### Realtime wifi strength monitoring

```bash
apt install wavemon
wavemon
```

### Other networking commands

```bash
sudo nmcli network off
sudo nmcli network on
sudo netplan try
sudo netplan apply
```

## get ip info

from [here](https://www.cyberciti.biz/faq/how-to-find-my-public-ip-address-from-command-line-on-a-linux/)

```bash
ifconfig
host myip.opendns.com resolver1.opendns.com
dig @resolver4.opendns.com myip.opendns.com +short
```

### get mac

```bash
arp -a <ip address>
```

<https://www.lifewire.com/find-a-mac-address-using-an-ip-address-818132>

### Wifi Scanning

```bash
nmcli d wifi
```

## Networking

```bash
nm-connection-editor
```

## Measuring Speed Between Computers

sudo apt install -y iperf

computer 1:

```bash
iperf -s
```

Computer 2:

```bash
iperf -c <other-computer-ip-or-hostname>
```

<https://superuser.com/questions/1275043/measure-bandwidth-between-two-computer-in-a-lan>

## IPTables

List current policies

```bash
iptables -L -v
```

Set accept rule:

```bash
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
```

delete rules

```bash
iptables -F INPUT
iptables -F OUTPUT
iptables -F FORWARD
```

delete all rules

```bash
iptables -F
```

## Find currently connected interface

```bash
ip route get 1.1.1.1 | grep -Po '(?<=dev\s)\w+' | cut -f1 -d ' '
```

## External Resources

* <https://vitux.com/managing-network-interfaces-and-settings-on-ubuntu-24-04-with-nmcli/>
* <https://linuxconfig.org/how-to-restart-network-on-ubuntu-20-04-lts-focal-fossa>
* <https://kerneltalks.com/virtualization/how-to-reset-iptables-to-default-settings/>
* <https://kerneltalks.com/networking/basics-of-iptables-linux-firewall/>
