---
title: Finding Large Files in repos
---

```bash
git rev-list --all --objects | awk '{print $1}' | git cat-file --batch-check | sort -k3n | tail -50 | awk '{print $1}' > items
```

full bash script:

```bash
while read -r largefile; do
    echo $largefile | awk '{printf "%s %s ", $1, $3 ; system("git rev-list --all --objects | grep " $1 " | cut -d \" \" -f 2-")}'
done <<< "$(git rev-list --all --objects | awk '{print $1}' | git cat-file --batch-check | sort -k3nr | head -n 20)"
```