---
title: Configuring ROS2 over a Tailscale VPN on Ubuntu
weight: 30
tags:
- ros2
- ubuntu
- linux
- tailscale
summary: " "
---

## Prerequisites

This tutorial assumes you have already installed ROS2 on a PC, Raspberry pi, or virtual machine running Ubuntu.  For those tutorials, please see:

* [Installing ROS2 on a Raspberry Pi](/notebook/ros2/installing-ros2-on-a-rpiz2w/)
* [Installing ROS2 on a Virtual Machine](/notebook/ros2/installing-ros2-on-a-vm/)

## Instructions

### Installing and using tailscale

First, go to the administrative interface at tailscale.com and ensure that the magicdns feature is enabled.

Then in a terminal window, download and run the install script straight from tailscale:

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

Before starting up, adjust some settings to enable other features

```bash
sudo tailscale set --operator=$USER -accept-dns=true --accept-routes=true 
```

Follow the instructions and link provided on the terimal interface to register your new computer with your tailscale account.  you can do this in the device itself, or copy the link to the browser in your own pc if connecting remotely.

Finally, check that your install works:

```bash
tailscale status
```

You should see your computer listed

### Set up fastrtps

```bash
sudo apt install -y ros-humble-rmw-fastrtps-cpp
```

Create a configuration file for fastrtps.  replace ```[HOSTNAME1]``` and ```[HOSTNAME2]``` with the hostname or IP address of your computers as seen in the tailscale administrative interface.  If you anticipate the ip address changing, for example if one of the machines is a docker container without ip address permanence enabled, it is suggested to use the hostname.  This is only possible with "magicdns" enabled.

```bash
cat <<EOT | sudo tee /etc/fast_ts.xml
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
EOT
```

Note: you can add more peers as needed to add more devices to your ROS2 network:

```xml
<locator>
    <udpv4>
        <address>[HOSTNAMEX]</address> 
    </udpv4>
</locator>
```

Next, modify .bashrc 

```bash
sudo nano ~/.bashrc
```

it should look like the following example.  The new lines should ideally be added before the ```source /opt/ros/humble/setup.bash``` line:

```bash
#....there will be other code above this

export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
FASTRTPS_DEFAULT_PROFILES_FILE=/etc/fast.xml

#... the following lines should already be here.  Don't modify them

export ROS_DOMAIN_ID=0
export ROS_LOCALHOST_ONLY=0
source /opt/ros/humble/setup.bash
```

Next, save and close the file.  In a terminal, type

```bash
source ~/.bashrc
```

even better, close and reopen your terminal window, or if you really want to test your changes, restart the pc.

```bash
sudo reboot now
```

Once restarted, In a new terminal window,

```bash
ros2 run demo_nodes_cpp listener
```

in a separate terminal window, type

```bash
ros2 run demo_nodes_cpp talker
```

Finally, open up a separate computer that has been set up to work over tailscale and is added to the fast.xml config file.  It should work, no matter how it's connected to the internet!

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
