---
title: Installing Windows 11 on Virtualbox
tags:
- virtualbox
- windows
summary: ""
---

Settings that  worked  for  me

Skip unattended installation
200gb vhd (flexible size)
8192 Mb Ram
TPM: None
EFI On
Enable Secureboot: No

Processor screen
processors: 2
enable pae/nx
enable Nested FT-x / AMD-V

Graphics: 
92 Mb Video Mem
No hardware acceleration

TURN OFF NETWORKING

When you get to the Windows Setup Screen, type ```shift+f10```

```cmd
regedit
```

Navigate to ```HKEY_LOCAL_MACHINE\SYSTEM\Setup```

Create a new  key called ```LabConfig```

Create three new  ```DWORD``` Values:

* BypassTPMCheck
* BypassRAMCheck
* BypassSecureBootCheck

Set each to 1.


Continue with setup.

at network selection, type ```shift+f10``` again, and type

```cmd
oobe\bypassnro
```

the computer will restart setup, but this time you can bypass the networking step to continue with "limited" setup

## External Links

* <https://blogs.oracle.com/virtualization/post/install-microsoft-windows-11-on-virtualbox>
* oobe(out of box experience without microsoft account): <https://www.windowscentral.com/how-set-windows-11-without-microsoft-account>