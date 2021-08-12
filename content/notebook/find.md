---
title: Using the ```find``` command in bash
tags:
  - bash
  - linux
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


## External Resources

* <https://www.tecmint.com/35-practical-examples-of-linux-find-command/>
