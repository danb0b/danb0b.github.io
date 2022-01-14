---
title: Too Many Authentication Failures?
tags:
- ubuntu
- linux
- ssh
---

## 

```
Received disconnect from ########## port 22:2: Too many authentication failures
```

Add the ```IdentitiesOnly``` option to your config file

```bash
nano .ssh/config
```

```
Host <myhost>
   User <myusername>
   Hostname <myhostname>
   Port 22
   PreferredAuthentications publickey
   IdentityFile <path_to_key>
   IdentitiesOnly yes
```

## Resources

* <https://www.tecmint.com/fix-ssh-too-many-authentication-failures-error/>
