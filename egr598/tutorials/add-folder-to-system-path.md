---
title: add folder to path
class_name: egr598
---

1. go to file explorer
1. right click on my computer
1. on the left menu sele advanced system settings
1. click on environment variables
1. in the lower window, find the path variable, and click edit
1. (in windows 10), click edit text
1. Go to the *end* of the string, and paste in the following(with ";C:\path\to\folder;" replaced by folder you want to add).  **Important:** Make sure there are semicolons between each path.  Do not replace any other items in the path.  
```
;C:\path\to\folder;
```
