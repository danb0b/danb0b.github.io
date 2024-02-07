---
title: Installing and Setting up MQTT
weight: 99
tags:
- mqtt
- linux
- ubuntu
- iot
- embedded-systems
---

## Installation

```bash
sudo apt update
sudo apt install -y mosquitto mosquitto-clients
sudo snap install mqtt-explorer
```

## Example Setup

```bash
sudo cp /usr/share/doc/mosquitto/examples/mosquitto.conf /etc/mosquitto/conf.d/
```

## Firewall

If you have UFW set up make sure you add permission:

```bash
sudo ufw allow 1883
```

## Simple Setup

```bash
MYIP1="<put your first ip address here>"
MYIP2="<put your second ip address here>"
```


```bash
cat <<EOT > ~/mosquitto.conf
listener 1883 $MYIP1
listener 1883 $MYIP2
allow_anonymous true
EOT
sudo install -o root -g root -m 644 mosquitto.conf /etc/mosquitto/conf.d/mosquitto.conf
sudo systemctl restart mosquitto
rm ~/mosquitto.conf
```

## Advanced Setup

This setup could be used for many users, to limit footprint

```bash
MYIP="<put your ip address here>"
```

```bash
cat <<EOT > ~/mosquitto.conf
listener 1883 $MYIP
allow_anonymous true
max_inflight_messages 1
max_inflight_bytes 500
message_size_limit 100
max_queued_bytes 500
max_queued_messages 3
#memory_limit 2000000
EOT
sudo install -o root -g root -m 644 mosquitto.conf /etc/mosquitto/conf.d/mosquitto.conf
rm ~/mosquitto.conf
```

## Service Instructions

```bash
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
sudo systemctl status mosquitto
```

Other Useful commands

```bash
sudo systemctl restart mosquitto
sudo systemctl stop mosquitto
sudo systemctl disable mosquitto
```

## Related Pages

* See the docker [setup](/notebook/docker/mqtt-server/) page

## Other Resources

* <https://www.vultr.com/docs/install-mosquitto-mqtt-broker-on-ubuntu-20-04-server/>
* [About Keepalive](https://www.hivemq.com/blog/mqtt-essentials-part-10-alive-client-take-over/)
* <http://www.steves-internet-guide.com/mossquitto-conf-file/>

## Secure MQTT info

* <https://obrienlabs.net/how-to-setup-your-own-mqtt-broker/>
