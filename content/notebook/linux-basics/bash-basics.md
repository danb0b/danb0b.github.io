---
title: Bash Basics
tags:
- bash
- linux
summary: " "
---

## Arguments

short arguments *usually* have a single dash followed by a single character.  An example is ```ls -a```,  where ```-a``` is an additional flag/attribute that indicates to the ```ls``` command that you should list all files, even if hidden by a ```.```

long arguments *usually* have two dashes followed by a word or phrase (connected by dashes). An example is ```ls --all```,  where ```--all``` has the same meaning as ```-a``` above.

## Getting help

* ```<command> -h```: display help
* ```<command> --help```: display help (long form of argument)
* ```man <command>```
* or you can go to <https://explainshell.com>

## Most Common Commands

* ```cd <absolute or relative path>```: change directory to the path indicated
* ```ls```: list files in current directory
* ```ls -la```: list *all* files(```a```) in list format(```-l```)
* ```chown <username>:<groupname> <file or folder>```: change the owner of the file or folder
* ```chown -R <username>:<groupname> <file or folder>```: change the owner of the folder *recursively*
* ```chmod <0-7><0-7><0-7> <file or folder>```: change the owner:group:anyone permissions for a file
* ```chmod -R <0-7><0-7><0-7> <file or folder>```: change the owner:group:anyone permissions for a folder *recursively*
* ```chmod +x <file or folder>```: add execution permission to a file/folder
* ```sudo+<command>```
* ```mkdir <path>```: make a directory at path indicated
* ```mv <path1> <path2>```: move a file from first path indicated to second path indicated
* ```cp <path1> <path2>```: copy files from first path indicated to second path indicated
* ```cp -r <path1> <path2>```: copy files *recursively* from first path indicated to second path indicated
* ```rmdir <path>```: delete a folder at a given path (folder must be empty)
* ```rm <path1> ...```: delete a file at a given path(s)
* ```rm -rf <path> ...```: delete a file/folder at a given path(s) using the ```force``` and ```recursive``` option (removes folders too, be careful!) |
*

## Keystrokes

| key combineation               | meaning                                        |
| ------------------------------ | ---------------------------------------------- |
| ```ctrl+c```                   | stops execution of whatever is running in bash |
| ```ctrl```+```alt```+```t```   | opens up a new ```bash``` terminal window      |
| ```ctrl```+```shift```+```t``` | opens up a new ```bash``` tab                  |
| ```ctrl```+```shift```+```w``` | closes the current ```bash``` tab              |
| ```ctrl```+```shift```+```q``` | closes all ```bash``` tabs                     |

## Common environment variables

* ```$HOME```
* ```$USERNAME```
* ```$PWD```
* ```$USER```
* ```$PATH```
* ```$PYTHONPATH```

* ```printenv``` list all current environment variables
* ```export``` will save an environment variable across sessions

## Other common commands

* ```chown```
* ```chmod```
* ```sudo```
* ```ps```
* ```kill```
* ```killall```
* ```htop```
* ```grep```
* ```pwd```
* ```printenv```
* ```export```
* ```cat```
* ```login```
* ```shutdown```
* ```reboot```
* ``diff``
* ```rclone```
* ```cd```
* ```mv```
* ```rsync```
* ```scp```
* ```ssh```
* ```echo```
* ```mkdir```
* ```rm```
* ```rmdir```
* ```cp```
* ```touch```
* ```ln```
* ```chgrp```


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

```bash
sed -i "s/regex/replace/" file
```

or

```bash
sed -i "s|regex|replace|" file
```

To copy output to a new file

```bash
sed "s/regex/replace/" filein > fileout
```

## Recursively chown

```bash
#chown -R <owner> <folder_1> <folder_2> ... <folder_n>
chown -R user /home/user
```

## Misc

### Count files in bash

```bash
ls -l1 | wc -l
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

## close bash without saving history

```bash
unset HISTFILE && exit
```

or

```bash
history -c && history -w && exit
```

## External Resources

* <https://cheatography.com/davechild/cheat-sheets/linux-command-line/>
* from [here](https://www.cyberciti.biz/faq/how-to-show-recursive-directory-listing-on-linux-or-unix/)
* From [here](https://www.howtogeek.com/481766/how-to-use-the-tail-command-on-linux/)
* source: <https://devconnected.com/how-to-count-files-in-directory-on-linux/>
* from [here](https://devconnected.com/how-to-chown-recursive-on-linux/)
* <https://www.cyberciti.biz/faq/clear-the-shell-history-in-ubuntu-linux/>
* <https://www.geeksforgeeks.org/linux-commands-cheat-sheet/>
