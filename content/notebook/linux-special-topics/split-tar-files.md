---
title: Splitting and Merging tar files
tags:
- compression
- ubuntu
- bash
- linux
summary: " "
---


From here: <https://unix.stackexchange.com/questions/61774/create-a-tar-archive-split-into-blocks-of-a-maximum-size>

```bash
tar -cvpzf - "<my folder name>"/ | split -d -b 10G - "<my folder name>.tar.gz."
cat <my folder name>.tar.gz.* | tar xzvf -
```