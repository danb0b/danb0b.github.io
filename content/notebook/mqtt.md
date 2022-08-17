---
title: Installing and Setting up MQTT
weight: 99
tags:
- mqtt
- linux
- ubuntu
---

```bash
sudo apt update
sudo apt install -y mosquitto mosquitto-clients
#sudo cp /usr/share/doc/mosquitto/examples/mosquitto.conf /etc/mosquitto/conf.d/

echo "listener 1883 ip_address_1" >> ~/mosquitto.conf
echo "allow_anonymous true" >> ~/mosquitto.conf
echo "max_inflight_messages 1" >> ~/mosquitto.conf
echo "max_inflight_bytes 500" >> ~/mosquitto.conf
echo "message_size_limit 100" >> ~/mosquitto.conf
echo "max_queued_bytes 500" >> ~/mosquitto.conf
echo "max_queued_messages 3" >> ~/mosquitto.conf
echo "#memory_limit 2000000" >> ~/mosquitto.conf

sudo cp ~/mosquitto.conf /etc/mosquitto/conf.d/

sudo snap install mqtt-explorer
```

## Other Resources

* <https://www.vultr.com/docs/install-mosquitto-mqtt-broker-on-ubuntu-20-04-server/>
* [About Keepalive](https://www.hivemq.com/blog/mqtt-essentials-part-10-alive-client-take-over/)
