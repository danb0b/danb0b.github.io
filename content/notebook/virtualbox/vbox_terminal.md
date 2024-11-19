---
title: Controlling Virtualbox from the Terminal
tags:
  - terminal
  - bash
  - linux
  - windows
  - virtualbox
weight: 99
summary: ""
---


Starting/stopping/pausing a VM

Now the fun begins. First, you must know the name of the VM you want to run. To find a list of the VMs, issue the command

```bash
vboxmanage list vms
vboxmanage list runningvms
```

This command will display all the VMs, as well as their unique IDs, in a form that you can use (Figure B).

To find all the hard disk images, use the command:

```bash
vboxmanage list hdds
```

To learn more detail about a specific instance, type

```bash
vboxmanage showvminfo ubuntu
```

Say we want to run the "ubuntu" VM as a headless instance. To do this, you would issue the command:

```bash
VBoxManage startvm "ubuntu" --type headless
```

The VM will start up and hand you back your bash prompt. Your virtual server (if that's how you're using the VM) is now available to you.

If you need to pause that VM, issue the command:

```bash
VBoxManage controlvm "ubuntu" pause
```

To restart that paused VM, issue the command:

```bash
VBoxManage controlvm "ubuntu" resume
```

To shut down the VM, issue the command:

```bash
VBoxManage controlvm "ubuntu" poweroff
VBoxManage controlvm "ubuntu" acpipowerbutton
```

Remove a vm

```bash
vboxmanage unregistervm ubuntu22 --delete
```

### Snapshot management

```bash
VBoxManage snapshot <uuid|vmname>
VBoxManage snapshot <uuid|vmname> take <snapshot-name>
VBoxManage snapshot <uuid|vmname> delete <snapshot-name>
VBoxManage snapshot <uuid|vmname> restore <snapshot-name>
VBoxManage snapshot <uuid|vmname> restorecurrent
VBoxManage snapshot <uuid|vmname> edit <snapshot-name | --current>
VBoxManage snapshot <uuid|vmname> list [--details | --machinereadable]
VBoxManage snapshot <uuid|vmname> showvminfo <snapshot-name>
```

```bash
vboxmanage snapshot ubuntu list
```

### Convert a virtualbox image

```bash
VBoxManage convertfromraw  sda.dd  sda.vdi --format VDI
```

## External Links

* [tech republic -- how to run virtualbox virtual machines from the command line](https://www.techrepublic.com/article/how-to-run-virtualbox-virtual-machines-from-the-command-line/)
* <https://www.virtualbox.org/manual/ch08.html>
