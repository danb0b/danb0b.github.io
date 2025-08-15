---
title: Fail2Ban
tags:
- security
- firewall
- ubuntu
- linux
summary: " "
---

Derived from [here](https://blog.swmansion.com/limiting-failed-ssh-login-attempts-with-fail2ban-7da15a2313b):

```bash
sudo apt install -y fail2ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban 
sudo systemctl status fail2ban 
```

config fail2ban for ufw

```bash
echo "[DEFAULT]" | sudo tee -a /etc/fail2ban/jail.local
echo "banaction=ufw" | sudo tee -a /etc/fail2ban/jail.local
```

restart the service and check

```bash
sudo systemctl restart fail2ban 
sudo fail2ban-client status
sudo fail2ban-client status sshd
```

list all banned:

```bash
sudo zgrep 'Ban' /var/log/fail2ban.log*
```
