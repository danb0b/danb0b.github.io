---
title: Kobo Ebook Reader information
tags:
- epub
- e-reader
- kobo
---

This link was the most helpful overview: <https://www.linux-magazine.com/Online/Features/Basic-Hacks-for-Kobo-E-Readers>

## Disabling user id requirements

```bash
#cd /path/to/the/ereader/.kobo
/media/danaukes/KOBOeReader/.kobo
sqlite3 KoboReader.sqlite
```

in the sqlite3 prompt, type

```sql
INSERT INTO user(UserID,UserKey) VALUES('1','');
```

then type ```ctrl+d``` to exit

unplug the e-reader

## External Links

* <https://duckduckgo.com/?q=flash+kobo+nia+reader+firmware&t=fpas&ia=web>
* <https://wiki.mobileread.com/wiki/Kobo_Firmware>
* <https://wiki.mobileread.com/wiki/Kobo_Firmware_Releases>
* <https://pgaskin.net/KoboStuff/kobofirmware.html>
* <https://www.mobileread.com/forums/showthread.php?t=311227>
* <https://www.todoereaders.com/en/kindle-tricks.html>
* <https://www.mobileread.com/forums/showthread.php?t=185660>
* <https://duckduckgo.com/?q=how+to+fkash+custom+fiemware+kobo+nia&t=fpas&ia=web>
* <https://www.mobileread.com/forums/showthread.php?t=295612>
* <https://wiki.mobileread.com/wiki/Kobo_eReader_hacks>
* <https://www.mobileread.com/forums/showthread.php?t=337972>
* <https://blog.the-ebook-reader.com/2018/03/17/list-of-hacks-mods-and-add-ons-for-kobo-ereaders/>
* <https://github.com/koreader/koreader>
* <https://koreader.rocks/>
* <https://www.mobileread.com/forums/showthread.php?t=314220>

