---
title: Installing ROS2 on a Raspberry Pi
tags:
- ros2
- ubuntu
- linux
- tailscale
---


## Flashing

Make sure you 

* add your ssh key during flashing 
* setup wifi
* define a hostname

## Tailscale

* turn on magicdns

```bash
sudo tailscale set --operator=$USER -accept-dns=true --accept-routes=true 
```

## Installing

It's important to disable automatic updates as you should initiate it according to your own availability.  Otherwise, it will start updating the first time you get an internet connection.  To prevent that, uninstall the "unattended-upgrades" package.

```bash
sudo apt remove unattended-upgrades
```

if you get a message like:

```bash
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 2131 (uWaiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 2131 (unattended-upgr)   
```

```bash
sudo killall unattended-upgr
```

It's always a good idea to perform headless updates in a way that won't break if you lose your wireless connction.  for this I use tmux

```bash
sudo apt update
sudo apt install tmux
tmux
```

inside the tmux window:

update and upgrade

```bash
sudo apt update && sudo apt upgrade -y
exit
```

```bash
sudo reboot now
```

Install packages

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

Install ros2.  this follows the humble instructions

```bash
locale
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt upgrade
```

now for installing ros, we want the minimum required set.  therefore we are going to install the base package and a couple packages on top as needed, rather than the full desktop

```bash
sudo apt install ros-humble-ros-base
# not sure which one of these I actually did, but pretty sure I did the cpp version.
#sudo apt install ros-humble-examples-rclpy-minimal-subscriber ros-humble-examples-rclpy-minimal-publisher 
sudo apt install ros-humble-examples-rclcpp-minimal-subscriber ros-humble-examples-rclcpp-minimal-publisher 
source /opt/ros/humble/setup.bash
sudo apt-get install python3-rosdep
sudo rosdep init
rosdep update
sudo apt install ros-humble-rmw-cyclonedds-cpp
sudo apt install ros-humble-rmw-fastrtps-cpp
```

```bash
ros2 run demo_nodes_cpp talker
sudo apt install ros-humble-demo-nodes-cpp
ros2 run demo_nodes_cpp talker
```

install ifconfig to find your ip address

```bash
sudo apt install net-tools
ifconfig
```



fastrtps

```bash
cat <<EOT >> ~/fast_local.xml
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
                <!-- Repeat this part for each Tailscale peer, use Tailscale machine/host name (from the admin console) -->
                    <locator>
                        <udpv4>
                            <address><your-local-ip-address></address> <!-- or <address>Tailscale IPv4 address</address> -->
                        </udpv4>
                    </locator>
                    <!-- End repeat -->
                    <locator>
                        <udpv4>
                            <address><other-local-ip-address></address> 
                        </udpv4>
                    </locator>
                </initialPeersList>
            </builtin>
        </rtps>
    </participant>
</profiles>
EOT
sudo mv ~/fast_local.xml /etc/
```

```bash
cat <<EOT >> ~/fast_ts.xml
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
                <!-- Repeat this part for each Tailscale peer, use Tailscale machine/host name (from the admin console) -->
                    <locator>
                        <udpv4>
                            <address><hostname1></address> <!-- or <address>Tailscale IPv4 address</address> -->
                        </udpv4>
                    </locator>
                    <!-- End repeat -->
                    <locator>
                        <udpv4>
                            <address><hostname2></address> 
                        </udpv4>
                    </locator>
                </initialPeersList>
            </builtin>
        </rtps>
    </participant>
</profiles>
EOT
sudo mv ~/fast_ts.xml /etc/
```

```bash
sudo cp /etc/cyclonedds_local.xml /etc/cyclonedds.xml
sudo cp /etc/fast_local.xml /etc/fast.xml
```

setup .bashrc

```bash
#export CYCLONEDDS_URI=/etc/cyclonedds.xml
#export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

FASTRTPS_DEFAULT_PROFILES_FILE=/etc/fast.xml
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
echo "export ROS_DOMAIN_ID=0" >> ~/.bashrc
echo "export ROS_LOCALHOST_ONLY=0" >> ~/.bashrc
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc 
source ~/.bashrc
## close and reopen your terminal or
sudo reboot now
```

```bash
ros2 run demo_nodes_cpp listener
ros2 run demo_nodes_cpp talker
```

now try replacing the local ip addresses with tailscale ip addresses

```bash
sudo cp /etc/cyclonedds_ts.xml /etc/cyclonedds.xml
sudo reboot now
ros2 run demo_nodes_cpp listener
ros2 run demo_nodes_cpp listener
```

<!-- 
sudo apt install ros-humble-desktop
sudo apt install ros-humble-desktop
sudo apt search ros-humble*demo*
sudo apt search ros-humble*
sudo apt search ros-humble-de*
sudo apt search ros-humble-de
sudo apt search ros-humble-demo
sudo apt search ros-humble-exampl
sudo apt install ros-humble-desktop -->

## External Resources

https://adityakamath.hashnode.dev/ros-2-and-vpns

### Oter Resources

* <https://stackoverflow.com/questions/55723797/how-to-join-the-default-bridge-and-user-defined-bridge-with-docker-compose-v3>
* <https://github.com/docker/compose/issues/3012>
* <https://docs.docker.com/compose/compose-file/#network-mode>
* <https://duckduckgo.com/?t=ffab&q=how+to+use+docker+tailscale+to+expose+services+over+tailscale&ia=web>
* <https://tailscale.com/kb/1247/funnel-examples>
* <https://forum.tailscale.com/t/connecting-to-a-service-on-a-docker-container-through-tailscale/756>
* <https://forum.tailscale.com/t/using-tailscale-from-docker-containers/127>
* <https://web.whatsapp.com/>
* <https://duckduckgo.com/?t=ffab&q=tomography&ia=web>
* <https://duckduckgo.com/?t=ffab&q=docker+network+mode&ia=web>
* <https://docs.docker.com/network/>
* <https://duckduckgo.com/?q=using+ros2+over+tailscale&t=ffab&ia=web>
* <https://adityakamath.hashnode.dev/ros-2-and-vpns>
* <https://duckduckgo.com/?t=ffab&q=use+tailscale+with+docker+services&ia=web>
* <https://tailscale.dev/blog/docker-mod-tailscale>
* <https://duckduckgo.com/?t=ffab&q=run+multiple+commands+docker+compose&ia=web>
* https://rnorth.org/tailscale-docker/
* https://github.com/tailscale/tailscale/issues/504#issuecomment-787224358
* https://github.com/tailscale/tailscale/blob/main/Dockerfile
* https://github.com/tailscale/tailscale/issues/295
* https://hub.docker.com/r/tailscale/tailscale
* https://tailscale.com/blog/kubecon-21
* https://docs.docker.com/network/network-tutorial-standalone/
* https://docs.docker.com/compose/networking/
* https://docs.docker.com/engine/extend/plugins_network/
* https://tailscale.com/kb/1112/userspace-networking
* https://tailscale.com/kb/1278/tailscaled
* https://www.howtogeek.com/devops/how-to-use-multi-threaded-processing-in-bash-scripts/