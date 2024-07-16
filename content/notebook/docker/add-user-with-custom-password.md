---
title: Add a User in a Docker Container with a custom password
tags:
- docker
- linux
---

```bash
password="1YelloDog@"
pass=$(perl -e 'print crypt($ARGV[0], "password")' $password)
echo "$pass"
```

## External Resources

* <https://www.cyberciti.biz/tips/howto-write-shell-script-to-add-user.html>
