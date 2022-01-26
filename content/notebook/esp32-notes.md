---
title: ESP32 Notes
weight: 1
tags: 
  - python
  - mechatronics
  - microcontroller
  - embedded-systems
---

## Example Projects

* <https://randomnerdtutorials.com/projects-esp32/>

## External Links

* Official MicroPython [Page](https://micropython.org/download/esp32/)
* uPyCraft IDE [Github Repository](https://github.com/DFRobot/uPyCraft)

## Product Comparison

* <https://makeradvisor.com/esp32-development-boards-review-comparison/>

* <https://www.mouser.com/ProductDetail/Espressif-Systems/ESP32-DevKitC-32D?qs=%252BEew9%252B0nqrDsObWEpDx6YQ%3D%3D&mgh=1&gclid=CjwKCAjwybyJBhBwEiwAvz4G74ePru_-tQfWS_DEqBxOR0LHcscr8IffqZhiS-5BOsP_XoH8helCLRoCF3wQAvD_BwE>
* <https://www.mouser.com/ProductDetail/Espressif-Systems/ESP32-C3-DevKitC-02?qs=stqOd1AaK7%2F1Q62ysr4CMA%3D%3D>
* [mouser search](https://www.mouser.com/c/embedded-solutions/engineering-tools/embedded-processor-development-kits/?m=Espressif)
* [digikey search](https://www.digikey.com/en/products/filter/rf-evaluation-and-development-kits-boards/859?s=N4IgjCBcpgnAHLKoDGUBmBDANgZwKYA0IA9lANogAMIAusQA4AuUIAykwE4CWAdgOYgAvsQC0AFmQg0kLHiKkKIAGwBWAMywktISJAAmJflwNOx3N3QACACb4AblYBGJTJxt0hQA)

## ESP32 Dev Board WROOM info

<https://www.etechnophiles.com/esp32-dev-board-pinout-specifications-datasheet-and-schematic/>

## micropython general refs
* <https://docs.micropython.org/en/latest/esp32/quickref.html>
    * [webrepl](https://docs.micropython.org/en/latest/esp32/quickref.html?highlight=webrepl#webrepl-web-browser-interactive-prompt)

## Install micropython IDE


derived from [here](https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/)

* [Windows Instructions](https://randomnerdtutorials.com/install-upycraft-ide-windows-pc-instructions/)
* [Mac Instructions](https://randomnerdtutorials.com/install-upycraft-ide-mac-os-x-instructions/)
* [Linux Instructions](https://randomnerdtutorials.com/install-upycraft-ide-linux-ubuntu-instructions/)
* [Using VSCode](https://lemariva.com/blog/2018/12/micropython-visual-studio-code-as-ide)
* [Installing Thonny(randomnerd)](https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/)
* [Installing Thonny(microcontrollerslab)](https://microcontrollerslab.com/getting-started-thonny-micropython-ide-esp32-esp8266/)
    1. Installing

        ```bash
        sudo pip3 install thonny
	pip install thonny # use this if anaconda is installed
        ```

    1. Running

        ```bash
        thonny
        ```
 
## Flash $\mu$python


You will need the esptool from espressif ([github](https://github.com/espressif/esptool))



It can be installed via pip from command line:
```bash
pip install esptool
```

First erase the flash
```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
```
From then on program the firmware starting at address 0x1000:
```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin
```

* <https://micropython.org/download/esp32/>
* <https://randomnerdtutorials.com/flashing-micropython-firmware-esptool-py-esp32-esp8266/>
* <https://randomnerdtutorials.com/flash-upload-micropython-firmware-esp32-esp8266/>
* <https://micropython-docs-esp32.readthedocs.io/en/esp32_doc/esp32/tutorial/intro.html>


## Arduino Instructions

[Install Arduino](/notebook/computer-setup/03-common-tools)

Follow this [tutorial](https://randomnerdtutorials.com/installing-the-esp32-board-in-arduino-ide-windows-instructions/) to install ESP32 support on arduino

### Alert

If you have python3 installed and linked to python, you'll need to direct arduino to use it

```bash
echo "alias python=python3" >> .bashrc
```

then open arduino from the terminal

```bash
arduino
```

## Pinout

![from https://randomnerdtutorials.com/getting-started-with-esp32/](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/08/ESP32-DOIT-DEVKIT-V1-Board-Pinout-30-GPIOs-Copy.png)

## Examples

### MQTT

* [MQTT tutorial](https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/)
    * [umqttsimple.py](https://raw.githubusercontent.com/RuiSantosdotme/ESP-MicroPython/master/code/MQTT/umqttsimple.py) from [this github repo](https://github.com/RuiSantosdotme/ESP-MicroPython/tree/master/code/MQTT)
* [MQTT Example #2](https://boneskull.com/micropython-on-esp32-part-2/)
* [MQTT Example #3](https://github.com/gloveboxes/ESP32-MicroPython-BME280-MQTT-Sample/)

### Serial

* <https://docs.micropython.org/en/latest/library/machine.UART.html>
* <https://techoverflow.net/2020/02/22/micropython-esp32-minimal-uart-example/>

### Analog 

* <https://randomnerdtutorials.com/esp32-esp8266-analog-readings-micropython/>

    ![](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/04/analog_input_pot_esp32.png?resize=1024%2C436&quality=100&strip=all&ssl=1)

    ```python
    from machine import Pin, ADC
    from time import sleep

    pot = ADC(Pin(34))
    pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

    while True:
      pot_value = pot.read()
      print(pot_value)
      sleep(0.1)
    ```


## FAQ (from amazon)

    1
    vote

    Question:
    What board should be selected from the arduino esp32 support?
    Answer:
    Please use the NodeMCU-32S profile
    By Xiuxin Seller on September 17, 2018

    1
    vote

    Question:
    What is the size of the Flash memory on the module?
    Answer:
    4MB
    By Xiuxin Seller on March 11, 2019

    0
    votes

    Question:
    What is the processor clock speed (Mhz) ?
    Answer:
    The processor clock speed is 240 MHz, as indicated by esptool.py during "make flash:"

    Chip is ESP32D0WDQ6 (revision 1) … see more
    By Music Maker on April 1, 2019
    2500 Mhz
    By Xiuxin Seller on January 7, 2019
    Collapse all answers

    0
    votes

    Question:
    Where can I find a schematic, or any documentation at all? It came with zilch.
    Answer:
    https://github.com/Nicholas3388/LuaNode
    By Christian U. on May 2, 2019
    https://spacehuhn.com
    By GEORGE ALLEN on May 1, 2019
    Collapse all answers

    0
    votes

    Question:
    What board should I choose? I followed espressif git configurations
    Answer:
    problem with this one is it's too wide to fit on a standard breadboard.. you'll need to be creative. https://www.youtube.com/watch?v=RtUIegaN644
    By I'm Rich James on August 2, 2018

    0
    votes

    Question:
    why is there a capacitor soldered from the "en" button to some weird point on the board. this does not show up in the description
    Answer:
    It allows the board to automatically enter boot mode to receive code uploads. Otherwise, you have to hold the boot button during code upload.
    By Spaceboyr00 on March 9, 2020
    Sorry I don’t know the answer.
    By Americubariqueño on November 18, 2019
    Collapse all answers

    0
    votes

    Question:
    Does this board can read in analog values?
    Answer:
    Yes, there are 15 analog inputs and the analog voltages 0v to 3.3v map to digital values of 0 to 4095 respectively.
    By Larry J. on January 29, 2019
    THere are 2 ADC's Each with about 7 AI's. However, ADC 2 is not available when WiFi is active. So, yes its there, but not really
    By jt on July 22, 2019
    Collapse all answers

    0
    votes

    Question:
    Where can I find a pinout? Which pins are analog?
    Answer:
    Google search with name of the board
    By Dawid W. on August 18, 2021

    0
    votes

    Question:
    can this charge a lipo battery?
    Answer:
    You need additional module to charge a battery
    By Dawid W. on August 18, 2021

    0
    votes

    Question:
    What is the spacing on the mounting holes?
    Answer:
    approx. 47mm x 23.5mm (I never use the mounting holes, 30 soldered pins is more than enough)
    By Steve Weingart on August 18, 2021
    They fit a standard breadboard. So 1/10" or 2.54mm
    By Jerry Stephens on August 18, 2021
    46 x 18mm and 46 x 19mm on the other side as close as I can measure
    By Jim V on August 18, 2021
    The board is about quarter size in width
    By Dawid W. on August 18, 2021
    Collapse all answers 
