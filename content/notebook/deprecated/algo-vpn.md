---
title: Installing Algo VPN
tags:
- ubuntu
- linux
- security
weight: 99
summary: ""
---

## Introduction

It is sometimes necessary to create a virtual network to enable computers across a large distance to communicate as if on the same network.  This section deals with how to install such a service on a virtual machine.

## Instructions

### VM Install

1. create a new virtual machine
    1. turn off usb
    1. bridged mode networking
    1. set MAC address to something easy, like 000000000002
    1. share local directory ~/danaukes/share to /mnt/share
        1. In vm settings Create share at ~/share and /mnt/share
        1. Add idealab to vbxosf group:

            ```bash
            sudo groupadd vboxsf #create group vboxusers
            sudo usermod -a -G vboxsf idealab #adds user idealab to group vboxsf
            ```

        1. Sign out and back in
        1. change sharing settings

            ```bash
            chmod 777 /mnt/share
            ```

### Algo Install

1. update computer and install necessary packages

    ```bash
    sudo apt update
    sudo apt upgrade
    sudo apt install -y python3-virtualenv git nano ssh net-tools
    ```

1. install algo

    ```bash
    sudo -i #necessarysu in ubuntu
    cd /
    git clone https://github.com/trailofbits/algo.git
    chmod 775 algo
    cd /algo
    python3 -m virtualenv --python="$(command -v python3)" .env &&   source .env/bin/activate &&   python3 -m pip install -U pip virtualenv &&   python3 -m pip install -r requirements.txt
    ```

1. edit config file

    ```bash
    nano config.cfg
    ```

    1. add users
    1. disable "BetweenClients_DROP", "block_smb", and "block_netbios"
    1. disable dns encryption

    hit ```ctrl+s``` to save and ```ctrl+x``` to exit

1. (optional) shutdown the virtual machine and take a snapshot
    
    ```bash
    sudo shutdown now
    ```
    
    take a snapshot of the machine, then restart and reconnect
    
    ```bash
    sudo -i
    cd /algo
    ```

1. run algo installer

    ```bash
    ./algo
    ```

    1. provider: select "Install to existing Ubuntu 18.04 or 20.04 server"
    1. select all defaults except the below:
        1. retain pki keys - N (default)
        1. each user should have their own acct - N (default)
         
        summary: 
        
        ```
        algo_provider "local"
        algo_ondemand_cellular "False"
        algo_ondemand_wifi "False"
        algo_ondemand_wifi_exclude "X251bGw="
        algo_dns_adblocking "False"
        algo_ssh_tunneling "False"
        wireguard_enabled "True"
        dns_encryption "False"
        ```
    
    1. deploy to localhost
    1. public IP address or domain name of your server: confirm default of <my_dynamic_hostname>


1. You should see a message like this:
    ```
                "\"#                          Congratulations!                            #\"",
                "\"#                     Your Algo server is running.                     #\"",
                "\"#    Config files and certificates are in the ./configs/ directory.    #\"",
                "\"#              Go to https://whoer.net/ after connecting               #\"",
                "\"#        and ensure that all your traffic passes through the VPN.      #\"",
                "\"#                     Local DNS resolver 172.31.126.44, fd00::f:7e2c                   #\"",
                ""
            ],
            "    \"#        The p12 and SSH keys password for new users is <hidden>       #\"\n",
            "    ",
            "    "

    ```

1. copy configuation files to other machines for use
1. run your virtualbox image as a service so it starts automatically.
    * See <https://github.com/onlyfang/VBoxVmService> for windows insstructions
    * see </notebook/virtualbox-service/> for linux instructions.

### Configure Router

1. give your new algo VM a unique ip address
1. forward specific ports to vm
    1. 4160:4160 - doesn't apply to ubuntu installs
    1. 51820:58120

### Configure other Computers

1. Install linux client:

from here: <https://github.com/trailofbits/algo/blob/master/docs/client-linux-wireguard.md>

    ```bash
    sudo apt update && sudo apt upgrade
    sudo apt install -y wireguard openresolv
    ```

1. Install the config file to the WireGuard configuration directory on your linux client:

    ```bash
    sudo install -o root -g root -m 600 <username>.conf /etc/wireguard/wg0.conf
    ```

1. Start the WireGuard VPN:

    ```bash
    sudo systemctl start wg-quick@wg0
    ```

1. Check that it started properly:

    ```bash
    sudo systemctl status wg-quick@wg0
    ```

1. Verify the connection to the AlgoVPN:

    ```bash
    sudo wg
    ```

1. See that your client is using the IP address of your AlgoVPN:

    ```bash
    curl ipv4.icanhazip.com
    ```

1. Optionally configure the connection to come up at boot time:


    ```bash
    sudo systemctl enable wg-quick@wg0
    ```

1. To stop the service,

    ```bash
    sudo systemctl stop wg-quick@wg0
    ```

1. To disable the service,

    ```bash
    sudo systemctl disable wg-quick@wg0
    ```

## Note:

Don't use the virtual host with the virtual algo guest, it will kill external communication to/from the guest.

