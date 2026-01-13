---
title: Sonoff S31 Smart Plug Mod
tags: 
  - iot
  - tasmota
  - smart-home
  - smart-plug
---


## Steps

1. Pop off gray cover
1. Slide out white slidy corner pieces
1. unscrew three exposed screws
1. disassemble main board
1. make a quick jig for flashing:

    ![Figure](img_20220812_220924561.jpg)

    1. get 2 double-sided, 1x6 header pins
    1. plug one into a ftdi friend (adafruit)
    1. match up wires, ensuring RX --> TX and TX --> RX
    1. Configure the FTDI friend for 3.3v VCC and 3.3V logic
    1. pull out the 2 pins for D-RX and D-TX, they aren't used
1. press the button and align the new jig to the sonoff's pins
1. While connected, run the following two commands in order

    ```bash
    python -m esptool --port /dev/ttyUSB0 erase_flash
    python -m esptool --port /dev/ttyUSB0 write_flash -fm dout 0x0 Downloads/tasmota.bin
    ```
    
1. Find the tasmota device Wifi SSID, connect, and set up your home wifi
1. connect to the new ip address and configure further, from [here](https://siytek.com/how-to-set-up-tasmota-mqtt-auto-discovery-for-home-assistant/)

```bash
SetOption19 on
```

1. set up mqtt
   1. go to configuration --> mqtt
   2. define the server, port, and any other advanced settings you might need.


1. For ESP32 devices, get the tasmota32.factory.bin

```bash
esptool.py --chip esp32 --baud 921600 --before default_reset --after hard_reset write_flash -z --flash_mode dout --flash_size detect 0x0 tasmota32.factory.bin
```

1. relay pulse time


<https://tasmota.github.io/docs/Commands/#control>

## Resources

Sonoff Specific:

* <https://tasmota.github.io/docs/devices/Sonoff-S31/>
* <https://tasmota.github.io/docs/Flash-Sonoff-using-Raspberry-Pi/>
* <http://lukeknipe.com/s31-tasmota/>
* <https://www.youtube.com/watch?v=kKtLKjI4wA0>
* <https://templates.blakadder.com/sonoff_S31.html>
* <https://siytek.com/how-to-set-up-tasmota-mqtt-auto-discovery-for-home-assistant/>

Tasmota Documentation

* [Tasmota Docs](https://tasmota.github.io/docs/#license)
* [Tasmota Supported Devices Repository](https://templates.blakadder.com/)
* [Tasmota Supported Modules](https://tasmota.github.io/docs/Supported-Modules/)
