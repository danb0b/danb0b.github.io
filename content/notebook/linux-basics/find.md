---
title: Using the ```find``` command in bash
tags:
  - linux
  - ubuntu
  - bash
weight: 10
---

# Using the ```find``` command in bash

## Find files with ```find```

```bash
find [-flags] path -expression
find ~/ -iname "*.py"
```

## key arguments

> Note: ```find``` does not follow the same argument convention as many other commands.

* ```-iname```
* ```-name```
* ```-type d``` / ```-type f```
* ```-group``` / ```-user```
* negative (!)
* ... many others

## Examples

Find all files below the current directory that match "filename.txt"

> Note: ```find``` does not follow the same argument convention as many other commands.

```bash
find . -name filename.txt
```

Find all files below the current directory that start with "filena"

```bash
 find . -name "filena*"
```

Find files with a name, ignoring case

```bash
find . -iname "FileName.txt"
```

Find directories in "/" with name "Dirname"

```bash
find / -type d -name Dirname
```

Find all files of type "txt"

```bash
find . -type f -name "*.txt"
```

Exclude directories

```bash
find . -not \( -path ./miniconda3 -prune \) -name \*.py -print
```

## Find and Replace with find and sed

```bash
find . -type f -name "*.md" -print0 | xargs -0 sed -i 's/foo/bar/g'
```

## Find text in a certain file type

Combine with grep to find links in markdown files ending in .mp4

```bash
find . -iname "*.md" -exec grep -l '.mp4)' {} \+ 
```

Find "video_source" keys in yaml files ending in .yaml

```bash
find . -iname "*.yaml" -exec grep -l 'video_source:' {} \+ 
```

Excluding multiple directories

```bash
find . -not \( -path ./repos -prune -o -path ./zenbook-backup -prune -o -path "./.local" -prune -o -path ./.gradle -prune -o -path ./envs -prune  -o -path ./.vscode -prune -o -path ./.config -prune  \) -name "*code*" -type d
```

## find with maximum depth

```bash
find . -iname "*.docx" -maxdepth 2
```

## Ignore "permission denied" message

```bash
find . -iname "*50_Lines_of*" 2> >(grep -v 'Permission denied' >&2)
```

or simpler:

```bash
find . -iname "*50_lines_of*" 2>&1 | grep -v  "Permission denied"
```

or just use ```sudo```

```bash
sudo find . -iname "*50_lines_of*"
```

## Find all directories without username

```bash
find . -type d ! -user danaukes
```

## Find with max depth of four all files that end in either .py or .ipynb that contain cadquery

```bash
find . -maxdepth 4 \( -iname "*.py" -o -iname "*.ipynb" \) -exec grep -in cadquery {} \+
```

### Execute something on the results of find with xargs

```bash
find . -name '.gitignore' | xargs wc -l
```

### External Resources

* <https://www.geeksforgeeks.org/mindepth-maxdepth-linux-find-command-limiting-search-specific-directory/>
* <https://linuxhandbook.com/find-command-exclude-directories/>
* <https://www.baeldung.com/linux/find-exclude-paths>
* <https://www.tecmint.com/35-practical-examples-of-linux-find-command/>
