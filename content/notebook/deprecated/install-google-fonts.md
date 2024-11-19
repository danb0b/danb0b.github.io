---
title: Install Google Fonts
tags:
- ubuntu
- linux
summary: ""
---

The advice on whether to install these fonts is a bit outdated as many of the fonts are going "variable weight" which does not play nice with xetex and thus pandoc.  So the best thing to do would be to install an older version of google fonts, but I haven't found that older commit that works yet.

```bash
cd
mkdir ~/.fonts
cd ~/.fonts
git clone git://github.com/google/fonts.git
rm -rf fonts/ofl/cantarell
rm -rf fonts/ufl/ubuntu*
rm -rf fonts/.git
fc-cache -f
```
