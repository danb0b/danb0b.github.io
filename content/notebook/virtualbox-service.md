---
title: Start VirtualBox VM as a Service
tags:
  - ubuntu
  - linux
  - virtualbox
---

## Steps

### Ensure you are a member of vboxusers group

```bash
sudo usermod -a -G vboxusers $USER
```

### Create a script

```bash
cat <<EOT > vbox_vm_start@.service
[Unit]
Description=VirtualBox VM %I
After=network.target vboxdrv.service
Before=runlevel2.target shutdown.target

[Service]
User=<put_your_username_here>
Group=vboxusers
Type=forking
Restart=no
TimeoutSec=5min
IgnoreSIGPIPE=no
KillMode=process
GuessMainPID=no
RemainAfterExit=yes

ExecStartPre=/bin/sleep 30
ExecStart=/usr/bin/VBoxManage startvm %i --type headless
ExecStop=/usr/bin/VBoxManage controlvm %i acpipowerbutton

[Install]
WantedBy=multi-user.target
EOT

sed -i "s/<put_your_username_here>/$USER/" vbox_vm_start@.service
sudo cp vbox_vm_start@.service /etc/systemd/system/vbox_vm_start@.service
rm vbox_vm_start@.service
sudo systemctl daemon-reload
```

### Get vm name

make sure your virtual machine doesn't have a space in it.

```bash
vboxmanage list vms
```

save that

### Start Service

```bash
sudo systemctl enable vbox_vm_start@<name of VM>
sudo systemctl start vbox_vm_start@<name of VM>
sudo systemctl status vbox_vm_start@<name of VM>
sudo systemctl stop vbox_vm_start@<name of VM>
sudo systemctl disable vbox_vm_start@<name of VM>
sudo systemctl daemon-reload
```

## External References

* <https://www.pragmaticlinux.com/2020/10/start-a-virtualbox-vm-on-boot-with-systemd/>
* <https://kifarunix.com/autostart-virtualbox-vms-on-system-boot-on-linux/>
* [Windows instructions](https://github.com/onlyfang/VBoxVmService)
* [Alternate way, using native vbox approach](https://kifarunix.com/autostart-virtualbox-vms-on-system-boot-on-linux/)