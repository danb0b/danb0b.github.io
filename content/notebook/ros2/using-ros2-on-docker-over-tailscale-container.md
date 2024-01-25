---
title: Using ROS2 in a Docker container running Tailscale
---
## Introduction

This example shows you how to create a docker-compose based container that uses tailscale which has been installed within a container.

## Instructions

First, go to the administrative interface at tailscale.com and ensure that the magicdns feature is enabled.
This allows your computers to refer to each other by name rather than IP address.  

Another important tool for automating the creation of docker containers is the use of pre-defined authorization keys.  This tutorial assumes you have created and configured an auth key on tailscale already.  This should be stored in an environment variable you define called ```$DOCKERKEY_PERM```.  This can be stored in your .bashrc file or any of the other ways made possible by docker and docker-compose files

Next, pick a folder for housing your docker compose file.  I have mine setup in ```~/docker/ros2-tailscale/```


Create a folder called ```build```.  Inside the build foder create a file called ```DOCKERFILE``` and paste in the following contents:

```dockerfile
FROM osrf/ros:humble-desktop
    
ENV ROS_DOMAIN_ID=0
ENV ROS_LOCALHOST_ONLY=0
ENV FASTRTPS_DEFAULT_PROFILES_FILE=/root/shared/fast.xml
ENV RMW_IMPLEMENTATION=rmw_fastrtps_cpp

RUN apt update && \ 
    apt install -y \ 
    ros-humble-rmw-fastrtps-cpp
    
RUN apt update && apt install -y curl
RUN curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/focal.noarmor.gpg | tee /usr/share/keyrings/tailscale-archive-keyring.gpg >/dev/null && \
curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/focal.tailscale-keyring.list | tee /etc/apt/sources.list.d/tailscale.list && \
apt update && \
apt install -y tailscale
```

Create a file called ```docker-compose.yml``` and paste the following contents inside

```yaml
version: "3.9"
services:
  tailscaled:
    build: ./build
    volumes:
      - ./lib:/var/lib
      - /dev/net/tun:/dev/net/tun
      - ./shared:/root/shared
    hostname: docker-ub
    environment:
      - TS_ROUTES=10.0.0.0/8
      - TS_USERSPACE=0
      - TS_STATE_DIR=/var/lib/tailscale
      - TS_HOSTNAME=docker1
    cap_add: 
      - NET_ADMIN
      - NET_RAW
    command: bash -c "tailscaled & tailscale up --authkey ${DOCKERKEY_PERM} && source /opt/ros/humble/setup.bash && ros2 run demo_nodes_cpp talker"
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

This will download the required docker images, build a new image, and start the container.  The container continuously broadcasts a message over the network to the other computers listed in your fast.xml file.

You can modify the command to listen:

```yaml
command: bash -c "tailscaled & tailscale up --authkey ${DOCKERKEY_PERM} && source /opt/ros/humble/setup.bash && ros2 run demo_nodes_cpp listener"
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
