---
title: Enabling .NetFx 3.5 in windows 11
---

insert windows 11 installation media cdrom/iso

Make sure the command below points to the proper drive letter(in this case D)

```powershell
Dism /online /enable-feature /featurename:NetFX3 /All /Source:D:\sources\sxs /LimitAccess
```

## External Resources

https://www.makeuseof.com/how-to-fix-net-framework-35-installation-error-0x800f0950-in-windows-11/