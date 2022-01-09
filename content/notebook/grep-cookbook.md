---
title: Grep Cookbook
tags:
  - linux
  - ubuntu
  - grep
  - bash
weight: 10
---  

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

## more complex examples:

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
