from: <https://www.techrepublic.com/article/how-to-run-virtualbox-virtual-machines-from-the-command-line/>

Starting/stopping/pausing a VM

Now the fun begins. First, you must know the name of the VM you want to run. To find a list of the VMs, issue the command VBoxManage list vms. This command will display all the VMs, as well as their unique IDs, in a form that you can use (Figure B).

Say we want to run the "Ubuntu Server" VM as a headless instance. To do this, you would issue the command:

VBoxManage startvm "Ubuntu Server" --type headless

The VM will start up and hand you back your bash prompt. Your virtual server (if that's how you're using the VM) is now available to you.

If you need to pause that VM, issue the command:

VBoxManage controlvm "Ubuntu Server" pause --type headless

To restart that paused VM, issue the command:

VBoxManage controlvm "Ubuntu Server" resume --type headless

To shut down the VM, issue the command:

VBoxManage controlvm "Ubuntu Server" poweroff --type headless
