---
title: Controlling Virtualbox from the Terminal
tags:
  - terminal
  - bash
  - linux
  - windows
  - virtualbox
weight: 99
---


Starting/stopping/pausing a VM

Now the fun begins. First, you must know the name of the VM you want to run. To find a list of the VMs, issue the command VBoxManage list vms. This command will display all the VMs, as well as their unique IDs, in a form that you can use (Figure B).

Say we want to run the "Ubuntu Server" VM as a headless instance. To do this, you would issue the command:

```bash
VBoxManage startvm "Ubuntu Server" --type headless
```

The VM will start up and hand you back your bash prompt. Your virtual server (if that's how you're using the VM) is now available to you.

If you need to pause that VM, issue the command:

```bash
VBoxManage controlvm "Ubuntu Server" pause
```

To restart that paused VM, issue the command:

```bash
VBoxManage controlvm "Ubuntu Server" resume
```

To shut down the VM, issue the command:

```bash
VBoxManage controlvm "Ubuntu Server" poweroff
```

## External Links

* [tech republic -- how to run virtualbox virtual machines from the command line](https://www.techrepublic.com/article/how-to-run-virtualbox-virtual-machines-from-the-command-line/)

