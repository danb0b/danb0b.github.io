---
title: Galaxy Tab Cleanup
---

##

1. Install ADB
1. Find your device
   
    ./adb devices

    1. Solve any permissions issues (see below)
   
1. list Packages   

   ./adb shell pm list packages --user 0

1. Save list 

   ./adb shell pm list packages --user 0 ~/packages-initial.txt

1. Uninstall packages


    ./adb shell pm uninstall -k --user 0 <com.program.name.here>



    <https://gitlab.com/W1nst0n/universal-android-debloater/-/blob/master/lists/Samsung.sh?ref_type=heads>

1. Save final list

   ./adb shell pm list packages --user 0 ~/packages-initial.txt

1. My before-after [list](galaxy-programs.xlsx)

## Permissions issue

If you are getting the following error when trying to interact with an android device.

$ adb devices
List of devices attached
xxxxxxxx    no permissions (user in plugdev group; are your udev rules wrong?);

<https://stackoverflow.com/questions/53887322/adb-devices-no-permissions-user-in-plugdev-group-are-your-udev-rules-wrong>

I followed these steps and it worked.
Ensure you give permission to the device on the android side as well.