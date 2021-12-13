---
title: Reverse SSH Tunnel
---

## Installation

```bash
sudo apt install autossh
```

set up logging:

```bash
echo 'export AUTOSSH_LOGFILE="$HOME/autossh.log"' >> ~/.bashrc
```

## Usage

```bash
autossh -M 20000 -fNn your_public_server -R 1234:localhost:22 -C
```

* ```-M```: the monitor port
* ```-f```: run in background
* ```-N```: no execution, just for forwarding
* ```-n```: redirect stdin to /dev/null
* ```-T```: disable pseudo terminal emulation
* ```-R```: 
* ```-C```: compress all data

```bash
autossh -f -nNT -i ~/keypair.pem -R 2000:localhost:22
```

## optional

start at reboot

```bash
crontab -e
```

enter the following

```
@reboot sleep 300 && autossh -M 20000 -f -Nnt -R 2201:localhost:22 <servername> -C
```

## External References

* <https://superuser.com/questions/37738/how-to-reliably-keep-an-ssh-tunnel-open>
* <http://www.debianadmin.com/autossh-automatically-restart-ssh-sessions-and-tunnels.html>
