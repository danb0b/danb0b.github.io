---
title: Arduino Setup Tutorial
//subtitle:
class_name: EGR598
---

# Arduino IDE and pro trinket setup

Refer to the [website](https://www.adafruit.com/product/2000) for all the documentation and files


1. Install the [Arduino IDE](https://www.arduino.cc/)
1. Install Adafruit [windows drivers](https://learn.adafruit.com/adafruit-arduino-ide-setup/windows-setup)(if applicable)
1. Add repository
    * file --> preferences
    * in "additional board managers", type "https://adafruit.github.io/arduino-board-index/package_adafruit_index.json"
1. Add adafruit boards manager
    * tools --> board --> board manager...
    * search for adafruit, select, and install.

### USB Bootloader Settings

1. Plug in USB Bootloader
1. Select Board:
    * ProTrinket5V/16MHz(USB)
1. Select Programmer:
    * USBTinyISP
1. upload

### USB/Serial Cable Settings

1. Plug in USB/Serial Cable to the six pins at the end of the adafruit pro trinket
1. If necessary, install [ftdi drivers](http://www.ftdichip.com/Drivers/VCP.htm)
1. Select Board:
    * ProTrinket5V/16MHz(FTDI)
1. Select Port (use device manager to identify)
1. Select Programmer:
    * AVR ISP
1. upload

<!--## Getting an arduino working with an RC Servo Motor
```{C}
asdf
```
-->

# Working with serial

### Serial Echo

```{C}
void setup() {
  Serial.begin(9600);
}
void loop() {
  if (Serial.available()) {      // If anything comes in Serial (USB),
    Serial.read();
    Serial.write("x");   // read it and send it out Serial1 (pins 0 & 1)
  }
}
```
