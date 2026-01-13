---
title: Home Assistant Setup
tags:
  - home-assistant
  - virtualbox
---

## Install Virtualbox

```bash
sudo apt install -y virtualbox virtualbox-ext-pack
sudo usermod -a -G vboxusers $USER
```

## Download Home Assistant

```bash
cd Downloads
wget https://github.com/home-assistant/operating-
system/releases/download/8.5/haos_ova-8.5.vdi.zip

unzip haos_ova-8.5.vdi.zip
```


## Create Virtual Machine

```bash
mkdir "/home/danaukes/VirtualBox VMs"
mkdir "/home/danaukes/VirtualBox VMs/home-assistant"
mv /home/danaukes/Downloads/haos_ova-8.5.vdi "/home/danaukes/VirtualBox VMs/home-assistant/"
vboxmanage createvm --name home-assistant --basefolder "/home/danaukes/VirtualBox VMs/"
vboxmanage registervm '/home/danaukes/VirtualBox VMs/home-assistant/home-assistant.vbox'
vboxmanage modifyvm home-assistant --memory 2000
vboxmanage modifyvm home-assistant --firmware efi`
vboxmanage modifyvm home-assistant --ostype Ubuntu_64
vboxmanage modifyvm home-assistant --nic1 bridged
vboxmanage modifyvm home-assistant --bridgeadapter1 eno1

vboxmanage storagectl home-assistant --name "SATA" --add sata --controller IntelAhci       
VBoxManage storageattach home-assistant --storagectl "SATA" --port 0 --device 0 --nonrotational on --discard on --type hdd --medium haos_ova-8.5.vdi
vboxmanage startvm home-assistant --type headless
```

## Set up service


## Connect
1. find the ip address of the new VM
1. over a vpn, set up tunneling

```bash
ssh -L 8123:192.168.202:8123 -C -N controller
```

## Configure

1. create account
	1. set name
	2. set map
	3. set currency to "USD"

## enable advanced mode
1. go to profile
2. select advanced mode

## Add integrations

### tasmota

### mqtt
server info:
- 192.168.0.120
- port 1883
- empty username
- empty password

### enphase

- username: envoy
- password: last 6 digiets of serial

### Nexia / American Standard / Trane
1. search for  nexia
2. select american standard
3. use username and password from asair.com website

### roku

### [ ] add SRP


## disable integrations
* radio
* spotify

## Add-Ons

### grafana
* enable startup, watchdog, and show in side menu

### terminal & ssh
* requires advanced mode
* enable startup, watchdog, and show in side menu

### hacs
<https://hacs.xyz/docs/setup/download/>


## Delete VM

```bash
vboxmanage unregistervm --delete home-assistant
```

## Docker version

```yaml
version: '3'
services:
  homeassistant:
    container_name: homeassistant
    image: "ghcr.io/home-assistant/home-assistant:stable"
    volumes:
      - ./config:/config
      - /etc/localtime:/etc/localtime:ro
    restart: unless-stopped
    privileged: true
    network_mode: host
```

## Resources

* <https://www.home-assistant.io/installation/linux>
* <https://docs.oracle.com/en/virtualization/virtualbox/6.0/user/vboxmanage-createvm.html>
* <https://docs.oracle.com/en/virtualization/virtualbox/6.0/user/vboxmanage-modifyvm.html>
* <https://docs.oracle.com/en/virtualization/virtualbox/6.0/user/vboxmanage-registervm.html>
* <https://andreafortuna.org/2019/10/24/how-to-create-a-virtualbox-vm-from-command-line/>
* <https://docs.oracle.com/en/virtualization/virtualbox/6.0/user/vdis.html>

- https://www.home-assistant.io/integrations/tasmota/
- [Download | HACS](https://hacs.xyz/docs/setup/download)
