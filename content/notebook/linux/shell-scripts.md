---
title: Shell Script Examples
tags:
- linux
- bash
- sh
summary: " "
---

How to find the directory of the script

```bash
#!/bin/bash
MY_PATH="`dirname \"$0\"`"

$MY_PATH/relative/path/to/other/file
```

pass arguments on to another script

```bash
$@
```

for example

```bash
#!/bin/bash
MY_PATH="`dirname \"$0\"`"

python3 $MY_PATH/my-script.py "$@"
```