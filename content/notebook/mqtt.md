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
cat <<EOT | tee ~/mosquitto.conf
listener 1883
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
cat <<EOT | tee ~/mosquitto.conf
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
* <http://www.steves-internet-guide.com/mqtt-username-password-example/>

## Secure MQTT info

* <https://obrienlabs.net/how-to-setup-your-own-mqtt-broker/>



## More recent links related to SSL/TLS

* <https://crodrigues.com/setting-up-a-secure-mosquitto-mqtt-broker-with-ssl-tls-and-user-access-control-mqtt-series-2/>
* <https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-debian-10>
* <https://mosquitto.org/man/mosquitto-tls-7.html>
* <https://stackoverflow.com/questions/67628488/issues-establishing-a-secure-connection-to-mosquitto-broker-2-0-10-using-m2mqtt>
* <https://docs.micropython.org/en/latest/library/ssl.html#>
* <https://github.com/peterhinch/micropython-mqtt/tree/master>
* <https://forum.micropython.org/viewtopic.php?f=18&t=11906#p65746>
* <https://github.com/peterhinch/micropython-samples/blob/master/README.md#414-ntp-time>
* <https://serverfault.com/questions/806141/is-the-alert-ssl3-read-bytessslv3-alert-bad-certificate-indicating-that-the-s>
* <https://forum.micropython.org/viewtopic.php?t=4280>
* <https://github.com/orgs/micropython/discussions/13441>
* <https://github.com/orgs/micropython/discussions/10559>
* <https://github.com/JustinS-B/Mosquitto_CA_and_Certs>


ca_maker produces:

.
|-- CA
|   |-- ca_crt.der
|   |-- ca_crt.pem
|   |-- ca_crt.srl
|   `-- ca_key.pem
|-- DH
|   `-- dhp_ffdhe2048.pem
|-- clients
|   |-- ca_crt.der
|   `-- ca_crt.pem
|-- csr_files
|   `-- server_req.csr
`-- server
    |-- server_crt.pem
    `-- server_key.pem

client_maker produces in addition

.
|-- clients
|   `-- student
|       |-- ca_crt.pem
|       |-- student_crt.pem
|       `-- student_key.pem
|-- csr_files
|   `-- student_req.csr