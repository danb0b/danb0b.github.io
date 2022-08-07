---
title: Install and configure fail2ban
tags:
- security
- firewall
- ubuntu
- linux
weight: 200
---

Derived from [here](https://blog.swmansion.com/limiting-failed-ssh-login-attempts-with-fail2ban-7da15a2313b):

```bash
sudo apt install fail2ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban 
sudo systemctl status fail2ban 
```

enter interactive mode

```bash
sudo -i
```

config fail2ban for ufw

```bash
echo "[DEFAULT]" >> /etc/fail2ban/jail.local
echo "banaction=ufw" >> /etc/fail2ban/jail.local
exit
```

restart the service and check

```
sudo systemctl restart fail2ban 
sudo fail2ban-client status
sudo fail2ban-client status sshd
```