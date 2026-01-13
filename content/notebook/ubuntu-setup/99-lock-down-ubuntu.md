---
title: 99-Locking Down Ubuntu
tags:
- ubuntu
- linux
- security
weight: 999
---

1. Set bios admin password
1. check sudoers group, make other users non-admin
1. delete unused / unnecessary accounts
1. reset root password
1. lock all ssh keys with passphrase
1. ensure .ssh, keys folders have the right permissions
1. remove plaintext passwords from all .config files
1. make sure cloud connections require password to start and do not start automatically
1. encrypt all important configurations (eg rclone, syncthing, etc)
1. remove credential files from all samba configs
1. make normal user accts for any guests
1. disable remembering passwords in
    * firefox
    * thunderbird
    * other email programs
    * other browsers
1. Lock down SSH
    1. See [how to disable passwords over ssh](/notebook/ssh/disable-password-ssh/)
    1. enable [LUKS remote decrypt](/notebook/ssh/remote-hd-unlock.md)
1. install tor?
1. add bitwarden or other 2FA app
1. update frequently
1. encrypt hard drive
1. set up logging
1. set / update vnc passwords
1. check out AppArmor
1. enable global privacy control: https://blog.mozilla.org/netpolicy/2021/10/28/implementing-global-privacy-control/