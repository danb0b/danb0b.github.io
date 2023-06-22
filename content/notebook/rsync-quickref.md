---
title: Rsync Quickref
---

say we have two folders:

- foldera
    - a.txt
    - b.txt
    - .e.txt
- folderb
    - c.txt
    - d.txt

rsync -haviP foldera folderb

will create

- folderb
    - c.txt
    - d.txt
    - foldera
        - a.txt
        - b.txt
        - .e.txt

rsync -haviP foldera/ folderb

will result in

- foldera
    - a.txt
    - b.txt
    - c.txt
    - d.txt
    - .e.txt

rsync -haviP foldera/ folderb/

produces the same results

rsync -haviP --delete foldera/ folderb

will result in

- foldera
    - a.txt
    - b.txt
    - .e.txt

rsync -haviP foldera/* folderb

will result in

- foldera
    - a.txt
    - b.txt
    - c.txt
    - d.txt

without the hidden files

| option        | detail                                                                                                               |
| ------------- | -------------------------------------------------------------------------------------------------------------------- |
| -h            | human-readable file sizes                                                                                            |
| -z            | compress file data during the transfer                                                                               |
| -i            | output a change-summary for all updates                                                                              |
| --inplace     | don't make a copy of the file and rename on completion, just write to the file (good for local copies, within the computer) |
| -P            | show progress                                                                                                        |
| --no-compress | don't use compression during transfer at all                                                                         |
| -c            | use checksum                                                                                                         |

<https://superuser.com/questions/109780/how-to-speed-up-rsync-between-two-local-disks>
<http://www.staroceans.org/e-book/understanding-the-output-of-rsync-itemize-changes.html>
