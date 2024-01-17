---
title: Modify VM Machine Information
tags:
  - virtualbox
---

Sometimes its useful to declare your computer type in virtualbox as something other than a virtual machine.

## Step 1: Create a Random string generator

put the following lines in a script or paste them into bash before running the next lines

```bash
#!/bin/bash

get_random_string () {

    openssl rand -hex "${1}" | cut -c "1-${1}"

}
```
## Find the string that describes your desired VM

```bash
vboxmanage list vms
```

## Step 3: Modify VM properties

This works for non-UEFI bioses.

```bash
my_vm = 'Win10'

VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/pcbios/0/Config/DmiBIOSVendor" "American Megatrends Inc"
VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/pcbios/0/Config/DmiBIOSVersion" "2.1.0"
VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/pcbios/0/Config/DmiSystemVendor" "ASUSTek Computer"
VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/pcbios/0/Config/DmiSystemSerial" "$(__get_random_string 9)"
VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/ahci/0/Config/Port0/SerialNumber" "$(__get_random_string 20)"
VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/ahci/0/Config/Port0/FirmwareRevision" "$(__get_random_string 8)"
VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/ahci/0/Config/Port0/ModelNumber" "SEAGATE ST3750525AS"
```

For windows 11, though, or where UEFI is required, you need to change the commands a bit.


```bash
my_vm = 'Win11'

VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/efi/0/Config/DmiBIOSVendor" "American Megatrends Inc"
VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/efi/0/Config/DmiBIOSVersion" "2.1.0"
VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/efi/0/Config/DmiSystemVendor" "ASUSTek Computer"
VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/efi/0/Config/DmiSystemSerial" "$(__get_random_string 9)"
VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/ahci/0/Config/Port0/SerialNumber" "$(__get_random_string 20)"
VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/ahci/0/Config/Port0/FirmwareRevision" "$(__get_random_string 8)"
VBoxManage setextradata "${my_vm}" "VBoxInternal/Devices/ahci/0/Config/Port0/ModelNumber" "SEAGATE ST3750525AS"

exit
```

## External Resources

* <https://gist.github.com/W-Floyd/7ccf5e4f074939e403bed483f82a4042>
