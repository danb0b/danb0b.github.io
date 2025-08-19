---
title: Grep Cookbook
tags:
  - linux
  - ubuntu
  - grep
  - bash
weight: 10
summary: A cookbook of common ```grep``` commands
---  

Useful for finding files that contain text

Best flags

* ```-i```: ignore case
* ```-r```: recursive (search all files below indicated path)
* ```-n```: indicate line numbers
* ```-l```: just list files
* ```-I```: ignore binary files
* ```-E```: use "extended" regular expressions

```bash
# grep -[flags] "text string" path
grep -iIrl ssh-ed25519 ~/.ssh
grep -iIrn ssh-ed25519 ~/.ssh
```

regular expressions help: <https://regexr.com/>

## Other useful grep flags

* ```-v```: list what doesn't match
* ```-w```: list whole-word matches
* ```-F```: plain text match (no regex)

## Examples
## Using ```grep``` by itself

search for "searchtext", ignoring case, ignoring binary files, recurisvely search, with line numbers, in this folder.

```bash
grep -Iirn "searchtext" .
```

Just list filenames

search for "searchtext", ignoring case, ignoring binary files, recurisvely search, just returning filenames, in this folder.

```bash
grep -iIrl "searchtext" .
```

## more complex examples

```bash
grep --exclude-dir="**.git**" --exclude-dir="**.ipynb_checkpoint**" --exclude="*.png" --exclude="*.svg" -iIrn "searchtext" .
grep -Iirl --exclude=*.svg --exclude-dir=**anaconda3** --exclude-dir=**Trash** tmux ~/
```

## Using ```grep``` in a pipe

find all processes named python

```bash
ps aux | grep python
```

## with a specific filetype

```bash
grep -Iirl "hello" --include=*.{cc,h} 
```

## with newline

```bash
pcregrep -rIn -M "\n#{1} " --include=*.md .
```

## GUI

```bash
sudo apt install -y libgtk-3-dev
pip install rummage
```
