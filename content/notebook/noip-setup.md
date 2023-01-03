---
Title: NoIP Client Configuration
---
## To Make and Install the Client

1. Go to noip's [dynamic update client for ubuntu](https://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client-on-ubuntu/) (noip2)
1. follow directions up through making:

    You will be able to install No-IP.com’s DUC on Ubuntu in just a few minutes with Terminal.

1. Once you have opened your Terminal window, log in as the “root” user. You can become the root user from the command line by entering “sudo -s” followed by the root password on your machine.

    ```bash
    #cd /usr/local/src/
    cd ~/Downloads
    wget http://www.noip.com/client/linux/noip-duc-linux.tar.gz
    tar xf noip-duc-linux.tar.gz
    cd noip-2.1.9-1/
    sudo make install
    ```

1. select the appropriate interface, like ```eth0```

1. You will then be prompted to log in with your No-IP account username and password.

**Note:** If you get “make not found” or “missing gcc” then you do not have the gcc compiler tools on your machine. You will need to install these in order to proceed.

## To Configure the Client

As root again (or with sudo) issue the below command:

-   /usr/local/bin/noip2 -C (dash capital C, this will create the default config file)

You will then be prompted for your No-IP username and password, as well as the hostnames you wish to update. Be careful, one of the questions is “Do you wish to update ALL hosts.” If answered incorrectly, this could effect hostnames in your account that are pointing at other locations.

Now that the client is installed and configured, you just need to launch it. Simply issue this final command to launch the client in the background:

-   /usr/local/bin/noip2

## Create and Install noip2 as a Service

Improved instructions for installing as a service, from [here](https://askubuntu.com/questions/1089704/cant-get-service-noip2-to-start-on-boot):

Create the file /etc/systemd/system/noip2.service with the following content (and drop your init.d scripts):

```
cat <<EOT | sudo tee /etc/systemd/system/noip2.service
[Unit]
Description=No-ip.com dynamic IP address updater
After=network.target
After=syslog.target

[Service]
Type=forking
ExecStart=/usr/local/bin/noip2
Restart=always

[Install]
WantedBy=default.target
EOT
```

Then issue
```bash
sudo systemctl daemon-reload
```

```bash
sudo systemctl enable noip2
sudo systemctl start noip2
sudo systemctl status noip2
```

Other Useful commands: 

```bash
sudo systemctl stop noip2
sudo systemctl disable noip2
```

## Other Resources
* [different service file](https://gist.github.com/NathanGiesbrecht/da6560f21e55178bcea7fdd9ca2e39b5)   ([local copy](noip2.service))
* <https://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client>

