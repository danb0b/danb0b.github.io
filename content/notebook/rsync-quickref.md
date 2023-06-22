---
title: Rsync Quickref
---


## quick recipes

### Local

```
rsync -haviP --inplace --delete-before --no-compress /storage/nas/photos /media/danaukes/extreme-ssd/
rsync -haviP --inplace --delete-before --no-compress --exclude-from="/home/danaukes/code/code_scripts/rsync_ignore.txt" --delete-excluded "/home/danaukes" "/media/danaukes/extreme-ssd/zenbook-backup/" | tee -a ~/backup.txt
```

### Remote

```
rsync -zhaviP --delete-before--exclude-from="/home/danaukes/code/code_scripts/rsync_ignore.txt" --delete-excluded /home/danaukes/ storage:/storage/nas/zenbook-backup/danaukes | tee -a ~/backup.txt
```

## Folder help

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

| option                        | detail                                                                                                                      |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| -h                            | human-readable file sizes                                                                                                   |
| -z                            | compress file data during the transfer                                                                                      |
| -i                            | output a change-summary for all updates                                                                                     |
| --inplace                     | don't make a copy of the file and rename on completion, just write to the file (good for local copies, within the computer) |
| -P                            | show progress                                                                                                               |
| --no-compress                 | don't use compression during transfer at all                                                                                |
| -c                            | use checksum                                                                                                                |
| --exclude-from="filename.txt" | list of files to ignore                                                                                                     |
| --delete-excluded             | also delete excluded files from dest dirs                                                                                   |
| --dry-run or -n               | dry run option                                                                                                              |

## Exclude file

an example for my home backup

I exclude

git repositories
.config directories I don't care about.

```
- anaconda/*
- code/*
- code_external/*
- meeting_notes/*
- miniconda3/*
- notes/*
- papers/*
- projects/*
- proposals/*
- repositories/*
- snap/*
- websites/*
- .arduino15/*
- .audacity-data/*
- .bundle/*
- .cache/*
- .fontconfig/*
- .local/share/Trash*
- .local/share/icons/*
- .var/*
- .zoom/*
- .config/pulse/*
- .config/libreoffice/*
- .config/spyder-py3/*
- .config/systemd/*
- .googleearth/*
- .local/share/mendeleydesktop
- .mcc/*
```

## External Refs
<https://superuser.com/questions/109780/how-to-speed-up-rsync-between-two-local-disks>
<http://www.staroceans.org/e-book/understanding-the-output-of-rsync-itemize-changes.html>
