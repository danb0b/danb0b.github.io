---
title: Clone Windows to Virtual Machine
tags:
  - virtualbox
params:
  published: false
summary: " "
---


From [here](http://underpop.online.fr/v/virtualbox/configuring-the-bios-dmi-information-virtualbox.html):

> The DMI data VirtualBox provides to guests can be changed for a specific VM. Use the following commands to configure the DMI BIOS information. In case your Virtual Machine is configured to use EFI firmware you need to replace pcbios by efi in the keys. 
>
> If a DMI string is not set, the default value of VirtualBox is used. To set an empty string use "<EMPTY>".
>
> Note that in the above list, all quoted parameters (DmiBIOSVendor, DmiBIOSVersion but not DmiBIOSReleaseMajor) are expected to be strings. If such a string is a valid number, the parameter is treated as number and the Virtual Machine will most probably refuse to start with an VERR_CFGM_NOT_STRING error. In that case, use "string:<value>", for instance
> 
> VBoxManage setextradata "VM name" "VBoxInternal/Devices/pcbios/0/Config/DmiSystemSerial" "string:1234"
> 
> Changing this information can be necessary to provide the DMI information of the host to the guest to prevent Windows from asking for a new product key. On Linux hosts the DMI BIOS information can be obtained with
> 
> dmidecode -t0
> 
> and the DMI system information can be obtained with
> 
> dmidecode -t1

```
vboxmanage setextradata "my-guest-name" "VBoxInternal/Devices/pcbios/0/Config/DmiSystemSerial" "string:myserialnum"
```

7c7a91c7d1d9

-----------------------

vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiSystemVendor"  "LENOVO"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "20A7CTO1WW"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiSystemVersion" "GRET44WW (1.21 )"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiSystemSKU" "LENOVO_MT_20A7_BU_Think_FM_ThinkPad X1 Carbon 2nd"
VBoxManage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiSystemFamily"
#VBoxManage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiSystemSerial" "R901BPCA"
#VBoxManage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiSystemUuid" "6B35D381-52E1-11CB-B69C-BA65A3840C86"

vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiBoardVendor" "LENOVO"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "20A7CTO1WW"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiBoardVersion" "SDK0E50512 Std"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiBoardSerial" "W1KS4411331"

vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiProcManufacturer"  "DmiProcManufacturer"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiProcVersion"       "DmiProcVersion"

vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiBIOSVendor" "LENOVO"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiBIOSVersion" "GRET44WW (1.21 )"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiBIOSReleaseDate" "3/19/2015"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiBIOSReleaseMajor" "2"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiBIOSReleaseMinor" "7"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiBIOSFirmwareMajor" "1"
vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/efi/0/Config/DmiBIOSFirmwareMinor" "16"

vboxmanage setextradata sara-old-lenovo "VBoxInternal/Devices/ahci/0/Config/Port0/SerialNumber" "2442396D"
VBoxManage setextradata sara-old-lenovo "VBoxInternal/Devices/ahci/0/Config/Port0/FirmwareRevision" ""
VBoxManage setextradata sara-old-lenovo "VBoxInternal/Devices/ahci/0/Config/Port0/ModelNumber" "SEAGATE ST3750525AS"

VBoxManage internalcommands sethduuid "~/VirtualBox VMs/sara.vdi" "A2697D5F-730A-4E7B-ACDB-B29743A0A108"

------------------------------------------

## Get DMI information from Windows

* <https://www.addictivetips.com/windows-tips/find-disk-and-volume-guid-windows-10/>
* <http://gnuwin32.sourceforge.net/packages/dmidecode.htm>
* <http://www.fit-pc.com/wiki/index.php/How_to_retrieve_product_information_from_within_Windows_/_Linux>
* <https://www.maketecheasier.com/get-bios-version-information-in-windows/>
* <https://kb.stonegroup.co.uk/index.php?View=entry&EntryID=370>
* <https://docs.microsoft.com/en-us/powershell/scripting/samples/collecting-information-about-computers?view=powershell-7.2>


## External Links

* <https://docs.oracle.com/en/virtualization/virtualbox/6.0/admin/changedmi.html>
* <https://www.virtualbox.org/manual/ch09.html#changedmi>
* <https://www.virtualbox.org/manual/ch09.html#changeacpicust>
* <https://forums.virtualbox.org/viewtopic.php?f=8&t=79879>
* <https://forums.virtualbox.org/viewtopic.php?f=2&t=93671>
* <https://forums.virtualbox.org/viewtopic.php?f=8&t=51608>
* <https://www.virtualbox.org/manual/ch08.html>
* <https://superuser.com/questions/55561/how-can-i-change-the-bios-serial-number-in-virtualbox>
* [Solidworks Spoof](https://gist.github.com/W-Floyd/7ccf5e4f074939e403bed483f82a4042)
* <https://www.howtogeek.com/312883/how-to-shrink-a-virtualbox-virtual-machine-and-free-up-disk-space/>
* <https://community.spiceworks.com/how_to/148559-windows-10-physical-to-virtualbox>

