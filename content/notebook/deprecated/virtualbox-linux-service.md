---
title: Start Virtualbox as a Service in Linux
tags:
- virtualbox
- linux
- ubuntu
- bash
- systemd
summary: " "
---

```bash
sudo apt reinstall virtualbox-dkms virtualbox-ext-pack virtualbox-qt virtualbox
```

```bash
sudo nano /etc/default/virtualbox 
```

```bash
VBOXAUTOSTART_DB=/etc/vbox
VBOXAUTOSTART_CONFIG=/etc/vbox/autostartvm.cfg
```

or 

```bash
echo -e "VBOXAUTOSTART_DB=/etc/vbox\nVBOXAUTOSTART_CONFIG=/etc/vbox/autostartvm.cfg" | sudo tee /etc/default/virtualbox
```

```bash
sudo usermod -aG vboxusers danaukes
sudo mkdir /etc/vbox
sudo chgrp vboxusers /etc/vbox
sudo chmod g+w /etc/vbox
sudo chmod +t /etc/vbox
sudo chmod 755 /etc/vbox

sudo nano /etc/vbox/autostartvm.cfg
```

```bash
default_policy = deny

danaukes = {
    allow = true
    startup_delay = 10
}
```


```bash
VBoxManage setproperty autostartdbpath /etc/vbox/
```

```bash
VBoxManage controlvm "home-assistant" poweroff
vboxmanage modifyvm home-assistant --autostart-enabled on  --autostop-type acpishutdown
VBoxManage startvm home-assistant --type headless
```


```bash
sudo -i
cd /etc/init.d/
services=(vboxautostart-service vboxweb-service vboxballoonctrl-service)
base_url="https://www.virtualbox.org/svn/vbox/trunk/src/VBox/Installer/linux"
for service in "${services[@]}"
    do
      wget "${base_url}/${service}".sh -O "${service}" \
      && chmod +x "$service"  \
      && update-rc.d "$service" defaults 90 10
    done
```

```bash
sudo systemctl enable vboxautostart-service
sudo systemctl start vboxautostart-service
sudo systemctl stop vboxautostart-service
sudo systemctl disable vboxautostart-service
```

## Resources

* <https://kifarunix.com/autostart-virtualbox-vms-on-system-boot-on-linux/>
* <https://roamingthings.de/posts/vboxautostart-service/>
* <https://askubuntu.com/questions/1131056/virtualbox-web-service-missing-after-clean-installation-on-ubuntu-18-04-1-lts>
* <https://unix.stackexchange.com/questions/202826/how-to-start-virtual-box-service-on-linux>