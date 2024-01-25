---
title: Using ROS2 over VPNs in the Classroom
summary: The purpose of this tutorial is to provide a way to provide access to ROS2 style data collection between computers, when specific kinds of access to the users' network is restricted.
date: 2024-01-25
tags:
- ros2
- ubuntu
- linux
- tailscale
- rpi
- docker
- tailscale
- vpn
---

## Introduction

The purpose of this tutorial is to provide a way to provide access to ROS2 style data collection between computers, when specific kinds of access to the users' network is restricted.  

When I taught a new course in Spring 2023, titled _"Experimentation and Deployment of Robotic Systems"_, I was proficient in ROS, having deployed it in my own lab and used it in my PhD thesis a decade before, but I was not as familiar with the communication differences between ROS1 and ROS2.  It turns out these differences are significant when deploying ROS2 to a network you don't have control over.

This article helps find a way around these issues by using tailscale, a modern VPN implementation that uses wireguard under the hood for creating a flat, private, and efficient network between enrolled computers.  This approach helps overcome the limitations created by the security requirements of physical hardware, as you might find in academic or industrial settings.

### Background

ROS1 is a well known quantity and has been deployed successfully in classrooms before.  It is based on a custom messaging protocol built on top of TCP/IP, and requires a server PC to coordinate and relay messages through the network of other devices on the ROS network.  As long as two computers are on the same network and can send TCP packets to each other, they can send messages to each other using ROS.  _It is also **end of life**, and not a good tool for teaching on in the classroom._

> This ignores the finer points of ROS network design concepts and related issues, but it worked.

With the transition to ROS2, however, the underlying message transport system changed from a custom messaging protocol built on TCP to a standardized messaging interface (DDS) that allowed different vendors' messaging libraries to be used to supply specific DDS _implementations_.  Two of the most popular, CycloneDDS and FastRTPS, which have both served as the default middleware for various versions of ROS2, use UDP instead of TCP out of the box.  Furthermore, to eliminate the need for a "ROS Master" computer to coordinate communication, DDS implementations for ROS use UDP "Multicast" by default.   UDP multicast can be thought of as a way to broadcast UDP packets to a network's entire subnet.  This helps simplify setup and lowers the barrier to entry for adding a new computer to ROS2 communication network, but it assumes that the user has control of their own network hardware and can enable UDP multicast.  Unfortunately, school settings (as well as critical industrial networks), _UDP multicast may be disabled_ by default.  

> TL/DR: ROS2 didn't work for me by default on my school network because...security.

### Interview time

You may be wondering, "Why didn't you just bring your own router"?

* I did.  But plugging it into the school network is a no-no.  So then devices on my router wouldn't have internet access.

"What do you need internet access for?"  Aren't industrial networks supposed to be cut off from the internet?  Shouldn't ROS2 work without it?

* Ideally yes, but realistically no.  Turning off internet access prevents devices subscribed to it from downloading new packages, software updates, and _most importantly_, _connecting to services they expect to be there_.  In the case of the Turtlebot4 and the IRobot Create3 platform they are built on, this includes a custom, hardcoded NTP server used to set and synchronize time on the create3.

"Why does the create3 need that?"

* Computers need their clocks to be synchronized sometimes.  In the case of ROS2 and the create3 I believe the onboard clock might have been reset between hard resets.

"Why didn't you just download packages and updates and then switch to the disconnected private network once prepped?"

* Every second in the classroom is precious.  Spending 10 minutes getting computers switched over between networks eats into learning time.  Furthermore, we were operating "headlessly", meaning transitioning between wifi access points, already an error prone task, can render the device inaccessible if you type the SSID or wifi password in incorrectly.  This would mean pulling out the SD card and finding a computer to fix the issue in at best, or having to reset the wifi connection manually (different for each device).  This can kill a whole class period, even if only one or two students have pernicious issues.

## To the Solution

Here is my solution

### VPN Options

My solution involves setting everyone up on a VPN.  There are open-source and subscription services that could work, but I was interested in finding a solution that:

* was easy to set up for non experts
* supported a baked-in DNS-style solution so identifying computers on the network could be done by name rather than (potentially-ephemeral) IP address
* worked in the classroom and at home without re-configuration
* "free" to use if not FREE to use.
* ideally no reconfiguration required between home and school

I have used a number of VPN technologies in the past, but many/most require

* Custom certificates or keys generated and distributed to them
* A host server you connect to (as a client)
* Custom routing instructions set up on each PC.

I have used commercial VPNs in the past but these each needed some sort of server, which itself would need to be requistioned, set up, and networked.  I am not an expert at that and there weren't resources on campus for that.  I had also used (raw) wireguard in the past using [trailofbits'](https://trailofbits.github.io/algo/) wireguard setup before, but the setup was error prone and required repeatedly recreating it if you needed to define new clients.  There was also some weirdness in my routing setup, in that I couldn't get computers on the VPN to see each other across the network persistently.  I knew I didn't have the networking chops to identify corner cases and support a custom VPN solution for the semester.  So I turned to tailscale.

Tailscale is a commercial solution built on top of wireguard that eliminates many of the hurdles associated with setup and configuration of a custom wireguard vpn. It is a commercial product but has a generous free tier, permitting up to 100 devices on a single tailscale network.  It also supplies a service called "magic dns" that ties the computer's hostname (that you define) to a custom dns entry connected back to that computer's IP address.  For example, if my computer's hostname is "dans-dell-optiplex", you could go to "<http://dans-dell-optiplex/>" and find any websites that computer is hosting.  Handy!

Unlike Windows, Mac, or Desktop Linux, server-based linux uses a hand-coded networking configuration called netplan.  Most of the time, to force switching between wifi configurations, you need to modify the file, or switch between files.  If you do it wrong in headless mode, you may have to connect to a keyboard and screen or pull out the SD card from your raspberry pi.  I had suggested that students buy a cheap wifi access point for home and name it the same as the ASU wifi, so they could use their setup at home without switching wifi configurations.  That is the only solution I had to the final need listed above.  Any other good suggestions?

I have also heard of Husarnet, which is built around ROS2 support.  I was not familiar with this product and would have tried it next if my solution hadn't worked.

"But isn't a VPN going to slow down communication?"

* Yes, but think about the needs of a classroom vs industry.  I need this solution to always work, without the delays associated with switching between home and school or between internal and external networks.  We are not throughputting enormous amounts of data during most of the course.  Additionally, my selection of tailscale is good because wireguard is reported to have some of the lowest latency due the network topologies it supports.

### DDS Implementation

I had been using CycloneDDS on ROS2-galactic, as it was the default, but could not get it to work over my Tailscale network.  I [had previously gotten multicast support turned off in my CycloneDDS config](/notebook/ros2/configuring-unicast-dds-with-cyclone/) for unicast-only communiation on a local network, and though I suspect my issues were simply my .xml configuration, the documentation provided no similar examples for my use case, and I saw no-one else doing it on the web.  CycloneDDS also even purportedly supports TCP-based communiation, but again, I couldn't put together a working xml file based on the documentation alone.  Please let me know if you have working examples!

I did find a solution on [this site](<https://adityakamath.hashnode.dev/ros-2-and-vpns>) that uses FastRTPS instead.  It was an easy switchover.  FastRTPS is also supported by all the devices in my classroom, including:

* The Turtlebot4 image supplied by Clearpath
* the IRobot Create3 (though I haven't yet tested it)
* General linux virtual machines and docker images

### Implementations

I have tried and tested this solution on the following devices:

* A Raspberry Pi Zero 2W running ROS2-humble, as my stand-in for the Raspberry Pi 4 modules in the turtlebot
* A Virtualbox Image Running ROS2-humble with bridged networking
* The default Ros2-humble image using host-mode networking
* A custom docker image running ROS2-humble.

It should be noted that the host for these virtual machines is an Ubuntu machine.  Some details about the virtualbox and docker solution may need to change for a Windows host.

## The Solution

I have created separate tutorials for the following implementations, which can all be found [here](/notebook/ros2/):

### Notes about Tailscale setup

It is important to enable "magic dns" in your tailscale administrative settings.  This allows your computers to refer to each other by name rather than IP address.  Another important tool for automating the creation of docker containers is the use of pre-defined authorization keys.  These can be created and configured on tailscale as well.

## Testing

In terms of testing, I am able to connect the raspberry pi to my home's wifi access point and my computer to my phone's wifi tethering, **and it can send messages over the internet!**  There is significant latency and some message loss, but it works.  When connected on the same physical network, the latency and loss are much lower.  I still need to benchmark network speeds with it on vs over the bare network.
