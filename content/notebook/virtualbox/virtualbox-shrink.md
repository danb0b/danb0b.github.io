---
title: Shrinking Virtualbox Hard Drives
tags:
- virtualbox
- windows
summary: ""
---

Derived from these instructions on [HowToGeek](https://www.howtogeek.com/312883/how-to-shrink-a-virtualbox-virtual-machine-and-free-up-disk-space/)

In this tutorial we assume a linux host and a windows guest

1. Clean up files
1. Delete Unused programs
1. empty all recycle bins

    ```powershell
    Clear-Recycle-Bin -Force
    ```

1. delete winsxs: <https://helpdeskgeek.com/windows-11/what-is-the-winsxs-folder-why-is-it-huge-and-how-to-cleanup/>

    ```powershell
    DISM.exe /Online /Cleanup-Image /AnalyzeComponentStore
    DISM.exe /Online /Cleanup-Image /StartComponentCleanup
    Dism.exe /online /Cleanup-Image /StartComponentCleanup /ResetBase
    ```

1. Clean up system files (search for "disk cleanup" in start menu)
1. Turn off hibernate

    ```powershell
    powercfg.exe -h off
    ```

1. Turn off page file
1. Turn off system restore

    <https://www.howtogeek.com/5482/make-system-restore-use-less-space-in-windows-7/>

    control panel --> recovery --> config disable system protection

1. find and delete shadow copies and backups: 
    * <https://superuser.com/questions/1746099/system-volume-information-folder-huge>
    * <https://www.thewindowsclub.com/delete-volume-shadow-copies-in-windows>

1. limit size for shadow copies: 

    ```powershell
    #vssadmin Resize ShadowStorage /For=C: /On=C: /MaxSize=320MB
    vssadmin list shadowstorage /for=c:
    vssadmin list shadows /for=c:
    vssadmin delete shadows /for=c:
    vssadmin Resize ShadowStorage /For=C: /On=C: /MaxSize=1%
    ```

1. delete winreaagent folder: <https://www.majorgeeks.com/content/page/what_is_the_winreagent_folder_and_can_i_delete_it.html>

1. Delete / shrink serviceprofiles directory

    <https://superuser.com/questions/1635577/can-i-delete-files-from-c-windows-serviceprofiles-networkservice-appdata-local>

    ```powershell
    netsh branchcache flush
    ```

1. Remove edge: <https://www.lifewire.com/uninstall-microsoft-edge-4156669>

1. defrag hard drive

    ```powershell
    defrag c: /U /V
    ```

    <https://www.partitionwizard.com/clone-disk/optimization-not-available.html>

1. write zeros to hard drive

    ```cmd
    .\sdelete.exe c: -z   
    ```

   * [sdelete utility](https://technet.microsoft.com/en-us/sysinternals/bb897443)
   * [Instructions from HowToGeek](https://www.howtogeek.com/312883/how-to-shrink-a-virtualbox-virtual-machine-and-free-up-disk-space/)

1. Find the virtual hard drive you want to shrink.  In the host OS, type:

    ```bash
    VBoxManage list hdds
    ```

1. Execute the shrink command

    ```bash
    VBoxManage modifymedium disk "/path/to/disk" --compact
    ```
