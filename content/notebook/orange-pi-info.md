---
title: Orange Pi Zero2 Information
tags: 
- linux
- gpio
- i2c
- sbcs
---

```
sudo mv /etc/netplan/orangepi-default.yaml /etc/netplan/orangepi-default.yaml.bk
echo << EOL | sudo tee /etc/netplan/00-home.yaml
network:
    version: 2
    ethernets:
        eno1:
            addresses:
            - 192.168.0.140/24
            dhcp4: no
            dhcp6: no
            nameservers:
                addresses:
                - 1.1.1.1
                - 1.0.0.1
                - 8.8.8.8
                - 8.8.4.4
            optional: true
    wifis:
        wlan0:
            dhcp4: yes
            dhcp6: yes
            addresses:
            - 192.168.0.141/24
            nameservers:
                addresses:
                - 1.1.1.1
                - 1.0.0.1
                - 8.8.8.8
                - 8.8.4.4
            access-points:
                senorita-fussy-bubbles:
                    password: ic5D4CHJV0X3
            routes:
                - to: default
                  via: 192.168.0.1
EOL
```



```bash
sudo orangepi-config
```


sudo apt update
sudo apt install openssh-server tmux

From [here](https://ubuntu.com/tutorials/gpio-on-raspberry-pi#1-overview):


sudo apt install python3-lgpio
sudo apt install python3-pip
sudo apt install libpython3-dev

## OLED and SSD1306 Driver

- <https://www.amazon.com/Songhe-0-96-inch-I2C-Raspberry/dp/B085WCRS7C/ref=sr_1_4?crid=1NJ0QBLD94E5L&keywords=SSD1306&qid=1668732264>
- https://pypi.org/project/Adafruit-SSD1306/

```bash
sudo pip3 install Adafruit-SSD1306
```

## Other Resources

* Main [webpage](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-Zero-2.html)
* [Wiki Page](http://www.orangepi.org/orangepiwiki/index.php/Orange_Pi_Zero_2)
* <https://www.instructables.com/Orange-Pi-One-Python-GPIO-basic/>
* <https://www.youtube.com/watch?v=ruxkz7TlgM4>
* <https://github.com/eutim/OPI.GPIO>
* <https://github.com/vsergeev/python-periphery>
* <https://learn.adafruit.com/circuitpython-on-orangepi-linux/i2c-sensors-and-devices>
* <https://learn.adafruit.com/circuitpython-on-orangepi-linux/orange-pi-pc-setup>
* <https://circuitpython.org/blinka/orange_pi_zero2/>
* <https://www.tomshardware.com/news/orange-pi-zero2-small-powerful-cost-effective>

----------------

```bash
sudo apt-get install -y python3 git python3-pip
sudo apt-get install libgpiod2 python3-libgpiod
pip3 install gpiod
sudo apt update && sudo apt upgrade -y
sudo pip3 install --upgrade setuptools

sudo apt install -y python-smbus python-dev i2c-tools
sudo adduser $USER i2c

pip3 freeze - local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U
sudo bash
pip3 freeze - local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U

pip3 install adafruit-blinka


```

```
sudo find / -iname "sun50*"
```
got help from [here](https://forum.armbian.com/topic/24427-working-overlay-for-orangepi-zero-2-to-see-armbian-config/)

```bash
echo -e "overlays=uart2 uart3 i2c0 i2c1 i2c2 spi-spidev usbhost1 usbhost2 usbhost3\nparam_spidev_spi_bus=0" | sudo tee -a /boot/orangepiEnv.txt
```

```
overlay_prefix=sun50i-h5
overlays=uart1 uart2 uart3 i2c0 i2c1 i2c2 spi-spidev usbhost0 usbhost1 usbhost2 usbhost3 pwm
param_spidev_spi_bus=0
```

pip3 install --upgrade adafruit-blinka adafruit-platformdetect

pip install wiringop

cat /proc/device-tree/compatible 
sun50i-h616

sudo find / -iname "sun50i-h616*"


sudo pip3 install ./

https://github.com/orangepi-xunlong/wiringOP-Python

