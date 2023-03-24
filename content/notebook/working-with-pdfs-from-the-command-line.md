---
title: Working with pdfs from the command line
tags:
  - ubuntu
  - bash
  - pdf
---

## Merge pdfs from Bash

```bash
sudo apt install pdftk
```

```
pdftk file1.pdf file2.pdf cat output mergedfile.pdf
```

## Shrink a PDF from the command line

```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
```

## Convert to PDF-A

```bash
gs -dPDFA -dBATCH -dNOPAUSE -sColorConversionStrategy=UseDeviceIndependentColor -sDEVICE=pdfwrite -dPDFACompatibilityPolicy=2 -sOutputFile="outputfile.pdf" "inputfile.pdf"
```