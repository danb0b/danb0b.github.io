---
title: Performance Tips
---

* disable swap
* enable trim

```bash
sudo apt install -y util-linux
```

```bash
systemctl status fstrim
```

check swappiness

```bash
cat /etc/sysctl.conf | grep -i swappiness
```

```bash
echo "vm.swappiness = 10" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

apt clean - add to cron

adjust io scheduler: have to do in grub, how to incorporate with LUKS?

adjust logging
sudo nano /etc/rsyslog.conf


overclock?
cpupower


minimize access time updates: <https://www.baeldung.com/linux/solid-state-drive-optimization#minimize-access-time-updates>
    how to do it on LUKS device?
    
    noatime,nodiratime

sudo apt install -y smartmontools
sudo smartctl -a /dev/nvme0
sudo smartctl -a /dev/nvme0n1


store system cache in ram: <https://www.howtogeek.com/62761/how-to-tweak-your-ssd-in-ubuntu-for-better-performance/>

add to fstab
tmpfs /tmp tmpfs defaults,noatime,mode=1777 0 0

## External Resources

* optimizing for ssds
    * <https://www.howtogeek.com/62761/how-to-tweak-your-ssd-in-ubuntu-for-better-performance/>
    * <https://devicetests.com/optimizing-ubuntu-for-ssds-guide>
    * <https://www.baeldung.com/linux/solid-state-drive-optimization>
* general
    * <https://www.baeldung.com/linux/solid-state-drive-optimization>
* disabling swap
    * <https://askubuntu.com/questions/214805/how-do-i-disable-swap>
* fstrim
    * <https://dannyda.com/2019/12/16/ubuntu-linux-check-ssd-trim-status/>