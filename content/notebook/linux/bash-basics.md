---
title: Bash Basics
tags:
- bash
- linux
summary: " "
---



## Common environment variables

$HOME
$USERNAME
$PWD
$USER
$PATH
$PYTHONPATH

## Common commands

* chown
* chmod
* sudo
* ps
* grep
* pwd
* printenv
* export
* cat
* login
* shutdown
* reboot
* diff
* rclone
* cd
* mv
* rsync
* scp
* ssh
* echo


## close bash without saving history

```bash
unset HISTFILE && exit
```

or

```bash
history -c && history -w && exit
```

<https://www.cyberciti.biz/faq/clear-the-shell-history-in-ubuntu-linux/>

## sudo

to run something as root

```bash
sudo <command> [command options]
```

to run interactively as root

```bash
sudo -i
```

to run something as someone else

```bash
sudo -i -u <username>
```

run ```exit``` to leave that session

## Find/Replace

To change the file in place:

```
sed -i "s/regex/replace/" file
```

or

```
sed -i "s|regex|replace|" file
```

To copy output to a new file

```
sed "s/regex/replace/" filein > fileout
```

## Recursively chown

from [here](https://devconnected.com/how-to-chown-recursive-on-linux/)

```bash
#chown -R <owner> <folder_1> <folder_2> ... <folder_n>
chown -R user /home/user
```

## Misc

### Count files in bash

source: <https://devconnected.com/how-to-count-files-in-directory-on-linux/>

```bash
ls | wc -l
```

## octal file permissions

```bash
stat /path/to/filename
```

```bash
stat -c '%A %a %n' /path/to/filename
```

## Print your environment variables

```bash
printenv | grep ROS
```

## tail

From [here](https://www.howtogeek.com/481766/how-to-use-the-tail-command-on-linux/)

see the last few lines

```bash
#tail -100 <filename>
tail -100 history.txt
```

see real-time changes to files as they get appended:

```bash
tail -f history.txt
```

see line 196-200 of a file

```bash
head -200 history.txt | tail -5
```

## Recursively list files

from [here](https://www.cyberciti.biz/faq/how-to-show-recursive-directory-listing-on-linux-or-unix/)

```bash
tree /path/to/dir
```

## Awk

```bash
awk '{print $1}' <filename>
```

```bash
cat <filename> | awk '{print $1}'
```

```bash
awk -E , '{print $1}' <filename.csv>
```
