---
title: Intricacies of working with two virtual machine clones
tags:
- docker
- virtualbox
---

Even if you have two vm clones with different mac addresses, you need to tell ubuntu how exactly the machine identifies itself on the network for the two clones to get separate ip addresses.  This is explained [here](https://superuser.com/questions/655670/two-virtualbox-vms-running-in-parallel-assigned-same-ip), but the easiest way to ensure it is to add ```dhcp-identifier: mac``` in your netplan config, as in:

```bash
      dhcp4: yes
      dhcp-identifier: mac
```

## External Resources

* <https://superuser.com/questions/655670/two-virtualbox-vms-running-in-parallel-assigned-same-ip>