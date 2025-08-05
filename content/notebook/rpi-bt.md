---
title: working with raspberry pi bluetooth from bash
---

open bluetoothctl in interactive mode from bash

```bash
bluetoothctl
```

This will create an interactive prompt for working with the bluetooth stack directly

```bash
list
select <my-MAC>
power on
discoverable on
scan on
pair <other-MAC>
scan off
exit
```

## External Resources

* <https://www.baeldung.com/linux/bluetooth-via-terminal>
