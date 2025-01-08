---
Title: NoIP Client Configuration
tags:
- ddns
- noip
summary: " "
---

## To  Install the Client

From here: <https://www.noip.com/support/knowledgebase/install-linux-3-x-dynamic-update-client-duc>

sudo apt update
sudo apt install -y net-tools

wget --content-disposition <https://www.noip.com/download/linux/latest>
tar xf noip-duc_3.1.1.tar.gz
sudo dpkg -i noip-duc_3.1.1/binaries/noip-duc_3.1.1_amd64.deb
sudo apt install -yf

noip-duc --username <username> --password <password> --hostnames <hostname> --ip-method 'aws-metadata' -v

## Create and Install noip2 as a Service

Improved instructions for installing as a service, from [here](https://askubuntu.com/questions/1089704/cant-get-service-noip2-to-start-on-boot):

Create the file /etc/systemd/system/noip2.service with the following content (and drop your init.d scripts):

```bash
cat <<EOT | sudo tee /etc/systemd/system/noip.service
[Unit]
Description=No-ip.com dynamic IP address updater
After=network.target
After=syslog.target

[Service]
Type=forking
ExecStart=/usr/bin/noip-duc --username <username> --password <password> --hostnames <hostname> --ip-method 'aws-metadata' -v
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
sudo systemctl enable noip
sudo systemctl start noip
sudo systemctl status noip
```

Other Useful commands:

```bash
sudo systemctl stop noip
sudo systemctl disable noip
```

-----

## From Source

1. Go to noip's [dynamic update client for ubuntu](https://www.noip.com/support/knowledgebase/install-linux-3-x-dynamic-update-client-duc#install_from_source) (noip3)
1. follow directions up through making:

    You will be able to install No-IP.com’s DUC on Ubuntu in just a few minutes with Terminal.

1. Once you have opened your Terminal window, log in as the “root” user. You can become the root user from the command line by entering “sudo -s” followed by the root password on your machine.

    prerequisites

    ```bash
    sudo apt update
    sudo apt install -yf build-essential
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    # unnecessary?
    #sudo apt install -y rustup
    ```

    close and reopen terminal or type ```source “$HOME/.cargo/env”```

    ```bash
    cd ~/Downloads
    wget https://dmej8g5cpdyqd.cloudfront.net/downloads/noip-duc_3.1.0.tar.gz
    tar xf noip-duc_3.1.0.tar.gz
    cd noip-duc_3.1.0
    cargo build --release
    sudo cp target/release/noip-duc /usr/local/bin
    ```

## Other Resources

* <https://gist.github.com/NathanGiesbrecht/da6560f21e55178bcea7fdd9ca2e39b5>
* Old
    * <https://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client-on-ubuntu/>
    * <https://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client>
