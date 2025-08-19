---
title: Shell Script Examples
tags:
- linux
- bash
- sh
summary: " "
---
## Sourcing bash scripts

```bash
source my_script
```

and

```bash
. my_script
```

are equivalent.  This is like copying and pasting each line from the file into your terminal emulator.

## Running bash scripts

you can run a bash script with the following command:

```bash
bash my_script
```

that does not mean it is executable.  to do that, you need to add a "shebang" with the executable's filepath to the top of the script.  For example,

```bash
#!/bin/bash
```

But that may not be the path of your bash program. How do you know what to put there?  What program do you want to run?
To find out the path of the program, use

```bash
which bash
```

ensure the script is executable:

```bash
chmod +x <filename>
```

then run the script

```bash
./my_script
```

## Other Shell Script Notes

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
