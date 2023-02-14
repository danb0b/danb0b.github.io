---
title: Logitech K380 function keys
---

* <https://support.logi.com/hc/en-us/community/posts/360037026053-k380-use-all-f1-f2-etc-keys-as-standard-function-keys->
* <https://www.radishlogic.com/tools/how-to-reverse-the-f-keys-of-logitech-k380-keyboard/>

Linux

* <https://askubuntu.com/questions/699138/logitech-k380-bluetooth-keyboard-make-function-keys-default>
* <https://www.radishlogic.com/tools/how-to-reverse-the-f-keys-of-logitech-k380-keyboard/>

Turn on the device and read dmesg:

```bash
sudo dmesg
```

```
hid-generic 0005:046D:B342.002E: unknown main item tag 0x0
input: Keyboard K380 Keyboard as /devices/pci0000:00/0000:00:08.1/0000:04:00.3/usb1/1-4/1-4:1.0/bluetooth/hci0/hci0:256/0005:046D:B342.002E/input/input77
hid-generic 0005:046D:B342.002E: input,hidraw11: BLUETOOTH HID v42.01 Keyboard [Keyboard K380] on 38:fc:98:48:d0:e0
```

## not quite working:

cat << EOT | sudo tee /etc/udev/rules.d/70-logi-k380.rules
ACTION=="add", SUBSYSTEM=="hidraw", KERNEL=="hidraw*", SUBSYSTEMS=="hid", KERNELS=="*:046D:B342.*", RUN+="/bin/bash -c \"echo -ne '\x10\xff\x0b\x1e\x00\x00\x00' > /dev/%k\""
EOT

sudo udevadm control --reload-rules && sudo udevadm trigger

## This works

echo -ne "\x10\xff\x0b\x1e\x00\x00\x00" | sudo tee /dev/[the device] # function keys default
echo -ne "\x10\xff\x0b\x1e\x01\x00\x00" | sudo tee /dev/[the device] # media keys default


## Better

<https://github.com/danb0b/external_k380-function-keys-conf>