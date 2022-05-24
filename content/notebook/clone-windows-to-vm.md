---
title: Clone Windows to Virtual Machine
tags:
  - virtualbox
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

## Get DMI information from Windows

* <http://gnuwin32.sourceforge.net/packages/dmidecode.htm>
* <http://www.fit-pc.com/wiki/index.php/How_to_retrieve_product_information_from_within_Windows_/_Linux>
* <https://www.maketecheasier.com/get-bios-version-information-in-windows/>
* <https://kb.stonegroup.co.uk/index.php?View=entry&EntryID=370>
* <https://docs.microsoft.com/en-us/powershell/scripting/samples/collecting-information-about-computers?view=powershell-7.2>


## External Links

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

