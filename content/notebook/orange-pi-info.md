---
title: Orange Pi Zero2 Information
tags: 
- linux
- gpio
- i2c
- sbcs
summary: " "
---

## Introduction

Note: the most important and helpful resource is the manual, which is available [here](https://drive.google.com/drive/folders/1T7NCV5ZBg1TrB1q_QUQ93GMbq0IlKLFn).

## Prepare the SD card

1. Copy the orange pi image over to an sd card
2. Expand the sd card
3. Update netplan.  Open up the sd card and modify the network config:

    ```bash
    sudo mv orangepi-default.yaml orangepi-default.yaml.bak
    cat << EOL | sudo tee 99-home.yaml
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
                dhcp4: no
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
                    <put your wifi ssid here>:
                        password: <put yoru wifi password here>
                routes:
                    - to: default
                      via: 192.168.0.1
    EOL
    sudo chmod 664 99-home.yaml
    ```

## Connect

With these changes you should be able to connect in a headless way

1. SSH

    ```
    ssh orangepi@192.168.0.141
    #default password is orangepi
    ```

1. update password

1. harden ssh:

    * <https://danaukes.com/notebook/ssh/ssh-reference/>
    * <https://danaukes.com/notebook/ssh/disable-password-ssh/>

1. Update Mirrors

edit /etc/apt/sources.list

```bash
deb http://ports.ubuntu.com/ubuntu-ports/ jammy main restricted universe multiverse
# deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy main restricted universe multiverse

deb http://ports.ubuntu.com/ubuntu-ports/ jammy-security main restricted universe multiverse
# deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-security main restricted universe multiverse

deb http://ports.ubuntu.com/ubuntu-ports/ jammy-updates main restricted universe multiverse
# deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-updates main restricted universe multiverse

deb http://ports.ubuntu.com/ubuntu-ports/ jammy-backports main restricted universe multiverse
# deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-backports main restricted universe multiverse
```

See this:<https://www.reddit.com/r/OrangePI/comments/16vdpjv/orange_pis_debian_and_the_chinese_update_servers/> and this: <http://www.orangepi.org/orangepibbsen/forum.php?mod=viewthread&tid=145250>

1. install tmux

    ```bash
    sudo apt update && sudo apt install -y tmux
    ```

    then open a new tmux window using the ```tmux``` command and upgrade your packages

1. (optional) install tailscale

    you can use [these instructions](/notebook/ubuntu-setup/01.2-tailscale/)

1. (optional, can do later) Upgrade

    ```bash
    sudo apt upgrade -y
    ```

    use ```ctrl+b``` then ```d``` to exit and let the install run.  You will need to check in periodically to intervene

1. (Optional) Set up orange pi config

    ```bash
    sudo orangepi-config
    ```

## Update systems

```bash
sudo adduser $USER i2c
echo "overlays=i2c3" | sudo tee -a /boot/orangepiEnv.txt && sudo reboot now
```

once restarted run

```bash
sudo i2cdetect -y 3
```

## Working with I/O

you will need some prerequisites:

```bash
#required
sudo apt install -y python3-pip swig python3-dev python3-setuptools
```

## (optional) Install WiringOP

```bash
orangepi@orangepi:~$ sudo apt update
orangepi@orangepi:~$ sudo apt install -y git
orangepi@orangepi:~$ git clone https://github.com/orangepi-xunlong/wiringOP
2) Compile and install wiringOP
orangepi@orangepi:~$ cd wiringOP
orangepi@orangepi:~/wiringOP$ sudo ./build clean
orangepi@orangepi:~/wiringOP$ sudo ./build
```

## Install wiringop-python

```bash
git clone --recursive https://github.com/orangepi-xunlong/wiringOP-Python.git
cd wiringOP-Python
find . -type f -name "*.c" -print0 | xargs -0 sed -i 's|/dev/i2c-[0-9]|/dev/i2c-3|g'
find . -type f -name "*.py" -print0 | xargs -0 sed -i 's|/dev/i2c-[0-9]|/dev/i2c-3|g'
python3 generate-bindings.py > bindings.i
pip3 install .
sudo pip3 install .
sudo python3 ~/wiringOP-Python/examples/orangepi-sensors/oled_ssd1306.py
```

to get it to run on startup,

```bash
(sudo crontab -u root -l; echo "@reboot python3 $HOME/wiringOP-Python/examples/orangepi-sensors/oled_ssd1306.py" ) | sudo crontab -u root -
```

got help from [here](https://stackoverflow.com/questions/42198960/how-to-add-a-crontab-job-to-crontab-using-a-bash-script)

## Other Resources

* **OLED:** <https://www.amazon.com/Songhe-0-96-inch-I2C-Raspberry/dp/B085WCRS7C/ref=sr_1_4?crid=1NJ0QBLD94E5L&keywords=SSD1306&qid=1668732264>
* Orange Pi
    * Main [webpage](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-Zero-2.html)
    * [Wiki Page](http://www.orangepi.org/orangepiwiki/index.php/Orange_Pi_Zero_2)
    * [Google Drive link](https://drive.google.com/drive/folders/1T7NCV5ZBg1TrB1q_QUQ93GMbq0IlKLFn) to user manuals, schematics
* Other Information (some outdated)
    * <https://www.instructables.com/Orange-Pi-One-Python-GPIO-basic/>
    * <https://www.youtube.com/watch?v=ruxkz7TlgM4>
    * <https://github.com/eutim/OPI.GPIO>
    * <https://github.com/vsergeev/python-periphery>
    * <https://learn.adafruit.com/circuitpython-on-orangepi-linux/i2c-sensors-and-devices>
    * <https://learn.adafruit.com/circuitpython-on-orangepi-linux/orange-pi-pc-setup>
    * <https://circuitpython.org/blinka/orange_pi_zero2/>
    * <https://www.tomshardware.com/news/orange-pi-zero2-small-powerful-cost-effective>

----

## Older Stuff

### Other packages it seems might be necessary

sudo apt install -y libgpiod2 python3-libgpiod
sudo apt install -y python3-smbus python3-dev i2c-tools  python3-lgpio
sudo apt install -y python3-dev python3-setuptools
pip3 install gpiod && sudo pip3 install gpiod

From [here](https://ubuntu.com/tutorials/gpio-on-raspberry-pi#1-overview):

### OLED and SSD1306 Driver

* <https://pypi.org/project/Adafruit-SSD1306/>

```bash
sudo pip3 install Adafruit-SSD1306
```

----------------

```bash
sudo apt install -y python3 git python3-pip
sudo apt install -y libgpiod2 python3-libgpiod
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

prior to clearing

```bash
#overlay_prefix=sun50i-h5
#overlay_prefix=sun50iw9-h5
#overlay_prefix=sun50i-h616
#overlays=uart1 uart2 uart3 i2c0 i2c1 i2c2 spi-spidev usbhost0 usbhost1 usbhost2 usbhost3 pwm
#overlays=uart2 uart5 i2c1 i2c2 i2c3 i2c4 spi-spidev pwm12 pwm34
#param_spidev_spi_bus=0
```

pip3 install --upgrade adafruit-blinka adafruit-platformdetect

pip install wiringop

cat /proc/device-tree/compatible
sun50i-h616

sudo find / -iname "sun50i-h616*"

sudo pip3 install ./

<https://github.com/orangepi-xunlong/wiringOP-Python>
