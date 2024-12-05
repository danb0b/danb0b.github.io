---
title: Setting up a Mosquitto MQTT server in docker.
summary: " "
---

## Docker compose

```yaml
version: "3"

services:
  mosquitto:
    image: eclipse-mosquitto
    container_name: mosquitto
    ports:
      - 1883:1883
      - 9001:9001
    volumes:
      - ./config:/mosquitto/config
      - ./data:/mosquitto/data
      - ./log:/mosquitto/log
```

## Config

also see [this page](/notebook/mqtt/) for general configuration ideas

```bash
persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log

listener 1883
allow_anonymous true
#password_file /mosquitto/conf/mosquitto.conf
```

## Related Pages

* [general mqtt page](/notebook/mqtt/)

## External Resources

* <https://techoverflow.net/2021/11/25/how-to-setup-standalone-mosquitto-mqtt-broker-using-docker-compose/>
* <https://hub.docker.com/_/eclipse-mosquitto>
* [home assistant tuning](https://www.homeautomationguy.io/docker-tips/configuring-the-mosquitto-mqtt-docker-container-for-use-with-home-assistant/)
* [random example](https://github.com/vvatelot/mosquitto-docker-compose/blob/master/docker-compose.yaml)
