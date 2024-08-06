---
title: Using the ```find``` command in bash
tags:
  - linux
  - ubuntu
  - bash
weight: 10
---

# Using the ```find``` command in bash

Find all files below the current directory that match "tecmint.txt"

```bash
find . -name tecmint.txt
```

Find all files below the current directory that start with "filena"

```bash
 find . -name "filena*"
```

Find files with a name, ignoring case

```bash
# find . -iname "FileName.txt"
```

Find directories in "/" with name "Dirname"

```bash
# find / -type d -name Dirname
```

Find all files of type "txt"

```bash
find . -type f -name "*.txt"
```

Exclude directories

```bash
find . -not \( -path ./miniconda3 -prune \) -name \*.py -print
```

## External Resources

* <https://www.tecmint.com/35-practical-examples-of-linux-find-command/>

## Find and Replace with find and sed

```bash
find . -type f -name "*.md" -print0 | xargs -0 sed -i 's/foo/bar/g'
```

## Find text in a certain file type

Find links in markdown files ending in .mp4

```bash
find . -iname "*.md" -exec grep -l '.mp4)' {} \+ 
```

Find "video_source" keys in yaml files ending in .yaml

```bash
find . -iname "*.yaml" -exec grep -l 'video_source:' {} \+ 
```

excluding directories

```bash
find . -not \( -path ./miniconda3 -prune \) -name \*.py -print  -exec grep -l 'html' {} \+ 
```

excluding multiple directories

```bash
find . \( -path ./.config -prune -o -path ./miniconda3 -prune -o -path ./.local -prune \) -o -iname "*.md" -exec grep -l 'esptool' {} \+ 
```

alternate:

```bash
find . -iname "*.py" ! -path './miniconda*' ! -path './.config*'  ! -path './apps*'  ! -path './.vscode*' ! -path '*zenbook-backup*' -exec grep -l 'import network' {} \+ 
```

tips from [here](https://linuxhandbook.com/find-command-exclude-directories/) and [here](https://www.baeldung.com/linux/find-exclude-paths)

## find with maximum depth

from [here](https://www.geeksforgeeks.org/mindepth-maxdepth-linux-find-command-limiting-search-specific-directory/)

```bash
find . -iname "*.docx" -maxdepth 2
```

## Ignore "permission denied" message

find . -iname "*50_Lines_of*" 2> >(grep -v 'Permission denied' >&2)

or simpler:

find . -iname "*50_lines_of*" 2>&1 | grep -v  "Permission denied"

## Find all directories without username

```bash
find . -type d ! -user danaukes
```

## Find with max depth of four all files that end in either .py or .ipynb that contain cadquery

```bash
find . -maxdepth 4 \( -iname "*.py" -o -iname "*.ipynb" \) -exec grep -in cadquery {} \+
```