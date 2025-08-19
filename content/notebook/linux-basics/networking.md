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

find all ports listening over TCP

```bash
sudo lsof -nP -iTCP -sTCP:LISTEN
```

similar command using netstat:

```bash
sudo netstat -tunlp
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

from here: <https://www.cyberciti.biz/faq/how-to-find-my-public-ip-address-from-command-line-on-a-linux/>

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

## nmap

find active computers on your network

```
sudo nmap -sn 192.168.0.1/24
```

## setting up your routing

You will want to find out what your gateway's address is.  With DHCP on and your system working, you can find it by displaying your current configuration ifconfig.

If running in a virtual machine, you can find it on your windows host with the following tutorial: <https://www.lifewire.com/how-to-find-your-default-gateway-ip-address-2626072>

install traceroute

```bash
sudo apt update && sudo apt install -y traceroute
```

Find your configured routes:

```bash
ip route
route -n
```

```bash
traceroute google.com
```

## Restart networking

```bash
sudo systemctl restart NetworkManager.service
sudo systemctl restart systemd-networkd.service
sudo netplan apply
sudo nmcli networking off
sudo nmcli networking on
```

## Connecting two subnets

* Machine 1
    * eth0: 192.168.185.1
    * eth1: 192.168.186.1
* Machine 2:
    * ens0: 192.168.185.2
* Machine 3:
    * ens0: 192.168.186.2

On Machine 1, enable Routing with

```bash
echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.conf
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p /etc/sysctl.conf
```

then forward packets between two subnets

```bash
sudo iptables -A FORWARD -i eth0 -j ACCEPT
sudo iptables -A FORWARD -i usb0 -j ACCEPT
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -t nat -A POSTROUTING -o usb0 -j MASQUERADE
```

On Machine 2:

```bash
sudo ip route add 192.168.186.0/24 via 192.168.185.1
```

On Machine 3:

```bash
sudo ip route add 192.168.185.0/24 via 192.168.186.1
```

## Find currently connected interface

```bash
ip route get 1.1.1.1 | grep -Po '(?<=dev\s)\w+' | cut -f1 -d ' '
```

## Remove NetworkManage (ubuntu)

```bash
sudo systemctl stop NetworkManager.service
sudo systemctl disable NetworkManager.service
sudo systemctl stop NetworkManager-wait-online.service
sudo systemctl disable NetworkManager-wait-online.service
sudo systemctl stop NetworkManager-dispatcher.service
sudo systemctl disable NetworkManager-dispatcher.service
sudo systemctl stop network-manager.service
sudo systemctl disable network-manager.service
sudo apt purge -y network-manager
```

from here: <https://askubuntu.com/questions/1091653/how-do-i-disable-network-manager-permanently>

## Disable cloud config

```bash
cat << EOF | sudo tee -a /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg
network: {config:disabled}
EOF
```

## External Resources

* <https://vitux.com/managing-network-interfaces-and-settings-on-ubuntu-24-04-with-nmcli/>
* <https://linuxconfig.org/how-to-restart-network-on-ubuntu-20-04-lts-focal-fossa>
* <https://kerneltalks.com/virtualization/how-to-reset-iptables-to-default-settings/>
* <https://kerneltalks.com/networking/basics-of-iptables-linux-firewall/>
* nmap
    * <https://www.shellhacks.com/20-nmap-examples/>
    * <https://serverfault.com/questions/153776/nmap-find-all-alive-hostnames-and-ips-in-lan>
    * <https://www.tecmint.com/nmap-command-examples/>
* routing
    * <https://shantoroy.com/raspberry%20pi/how-to-configure-raspberry-pi-as-gateway/>
    * <https://askubuntu.com/questions/1052789/correct-way-to-route-between-2-interfaces-with-netplan-in-ubuntu-18-04>
