---
title: Shrink a PDF from the command line
tags:
  - ubuntu
  - bash
  - pdf
---


```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
-dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
```
