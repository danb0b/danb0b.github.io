---
title: Using ROS2 over tailscale using docker host-mode networking
---

## Introduction

This example shows you how to create a docker-compose based container that uses "host-mode" networking

## Instructions

First, go to the administrative interface at tailscale.com and ensure that the magicdns feature is enabled.  
This allows your computers to refer to each other by name rather than IP address.  

> This setup requires that you have downloaded and installed virtualbox on your host machine (the computer running docker).  I have tested this with Ubuntu 22.04 and it works.

Next, pick a folder for housing your docker compose file.  I have mine setup in ```~/docker/ros2-host/```

Create a file called ```docker-compose.yml``` and paste the following contents inside

```yaml
version: '2'

services:
  ros1:
    environment:
    - ROS_DOMAIN_ID=0
    - ROS_LOCALHOST_ONLY=0
    - FASTRTPS_DEFAULT_PROFILES_FILE=/root/shared/fast.xml
    - RMW_IMPLEMENTATION=rmw_fastrtps_cpp
    container_name: ros2-talker
    image: osrf/ros:humble-desktop
    hostname: ros-host2
    domainname: test
    network_mode: host
    volumes:
      - ./shared:/root/shared
    command: bash -c "source /opt/ros/humble/setup.bash && ros2 run demo_nodes_cpp talker"
    restart: unless-stopped
```

create a subfolder called ```shared```.  Inside, create a file called ```fast.xml``` and paste in the following contents:

Replace ```[HOSTNAME1]``` and ```[HOSTNAME2]``` with the hostname or IP address of your computers as seen in the tailscale administrative interface.  If you anticipate the ip address changing, for example if one of the machines is a docker container without ip address permanence enabled, it is suggested to use the hostname.  This is only possible with "magicdns" enabled.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<profiles xmlns="http://www.eprosima.com/XMLSchemas/fastRTPS_Profiles">
    <transport_descriptors>
        <transport_descriptor>
            <transport_id>TailscaleTransport</transport_id>
            <type>UDPv4</type>
        </transport_descriptor>
    </transport_descriptors>
    <participant profile_name="TailscaleSimple" is_default_profile="true">
        <rtps>
            <userTransports>
                <transport_id>TailscaleTransport</transport_id>
            </userTransports>
            <useBuiltinTransports>true</useBuiltinTransports>
            <builtin>
                <initialPeersList>
                    <locator>
                        <udpv4>
                            <address>[HOSTNAME1]</address>
                        </udpv4>
                    </locator>
                    <locator>
                        <udpv4>
                            <address>[HOSTNAME2]</address> 
                        </udpv4>
                    </locator>
                </initialPeersList>
            </builtin>
        </rtps>
    </participant>
</profiles>
```

Note: you can add more peers as needed to add more devices to your ROS2 network:

```xml
<locator>
    <udpv4>
        <address>[HOSTNAMEX]</address> 
    </udpv4>
</locator>
```

Finally, try out the container using the command:

```bash
docker compose up
```

This will download the required docker images and start the container.  The container continuously broadcasts a message over the network to the other computers listed in your fast.xml file.

You can modify the command to listen:

```yaml
command: bash -c "source /opt/ros/humble/setup.bash && ros2 run demo_nodes_cpp listener"
```

or to start up your own custom nodes, which is outside of this example.

## External Resources

<https://adityakamath.hashnode.dev/ros-2-and-vpns>

### Oter Resources

* <https://stackoverflow.com/questions/55723797/how-to-join-the-default-bridge-and-user-defined-bridge-with-docker-compose-v3>
* <https://github.com/docker/compose/issues/3012>
* <https://docs.docker.com/compose/compose-file/#network-mode>
* <https://tailscale.com/kb/1247/funnel-examples>
* <https://forum.tailscale.com/t/connecting-to-a-service-on-a-docker-container-through-tailscale/756>
* <https://forum.tailscale.com/t/using-tailscale-from-docker-containers/127>
* <https://web.whatsapp.com/>
* <https://docs.docker.com/network/>
* <https://duckduckgo.com/?q=using+ros2+over+tailscale&t=ffab&ia=web>
* <https://adityakamath.hashnode.dev/ros-2-and-vpns>
* <https://duckduckgo.com/?t=ffab&q=use+tailscale+with+docker+services&ia=web>
* <https://tailscale.dev/blog/docker-mod-tailscale>
* <https://rnorth.org/tailscale-docker/>
* <https://github.com/tailscale/tailscale/issues/504#issuecomment-787224358>
* <https://github.com/tailscale/tailscale/blob/main/Dockerfile>
* <https://github.com/tailscale/tailscale/issues/295>
* <https://hub.docker.com/r/tailscale/tailscale>
* <https://tailscale.com/blog/kubecon-21>
* <https://docs.docker.com/network/network-tutorial-standalone/>
* <https://docs.docker.com/compose/networking/>
* <https://docs.docker.com/engine/extend/plugins_network/>
* <https://tailscale.com/kb/1112/userspace-networking>
* <https://tailscale.com/kb/1278/tailscaled>
* <https://www.howtogeek.com/devops/how-to-use-multi-threaded-processing-in-bash-scripts/>
