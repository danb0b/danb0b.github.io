---
title: Install Tailscale
weight: 12
tags:
  - vpn
  - linux
  - ubuntu
summary: how to install tailscale in linux
---

## Prerequisites

If you have a raspberry pi or docker image, you may need to install curl first:

```bash
sudo apt update && sudo apt install -y curl -y
```

## Generic Install script

> **Warning:** Never do this if you don't trust the source and haven't inspected the script.

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

### Starting

Start up tailscale with

```bash
sudo tailscale up
```

Follow the on-screen instructions.  You may have to copy/paste the link into your host's browser.

## Options

Good things to do once you have added your computer to your tailnet is to:

### disable key expiry

1. open up <https://login.tailscale.com/admin/machines>,
1. click on the ```...``` button next to the desired computer
1. select "disable key expiry"

### turn on magic dns

If using a service like tailscale, you can also enable their "magic dns" option, which makes devices on your "tailnet" available using their names on tailscale.

1. go to: <https://login.tailscale.com/admin/dns>
1. turn on "Enable Magic DNS"

Go here to learn more about setting it up: <https://tailscale.com/kb/1081/magicdns>

> I've found that this service sometimes does not work from within larger managed networks.  In this case, a hard-coded /etc/hosts file will still work.

## Delete tailscale cache

```bash
sudo tailscale down
sudo rm -rf /var/lib/tailscale
```

### External references

* <https://pkgs.tailscale.com/stable/#static>
