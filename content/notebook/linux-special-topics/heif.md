---
title: Dealing with .heif Images
tags: 
  - images
  - heif
  - ubuntu
  - bash
---



<https://linuxnightly.com/convert-heif-images-to-jpg-or-png-on-linux/>

```bash
sudo apt install -y libheif-examples
```

```bash
heif-convert image.HEIC new-image.jpg
```

using find...

```bash
find . -iname "*.heic" -exec heif-convert -q 100 {} {}.jpg \;
```
