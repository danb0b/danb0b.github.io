---
title: Grep Cookbook
tags:
  - grep
  - bash
  - linux
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
A more complex example:

```bash
grep --exclude-dir="**.git**" --exclude-dir="**.ipynb_checkpoint**" --exclude="*.png" --exclude="*.svg" -iIrn "searchtext" .
```

## Using ```grep``` in a pipe

find all processes named python

```bash
ps aux | grep python
```