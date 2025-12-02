---
title: Working with pdfs from the command line
tags:
  - ubuntu
  - bash
  - pdf
summary: " "
---

## Merge pdfs from Bash

```bash
sudo apt install -y pdftk
```

```bash
pdftk file1.pdf file2.pdf cat output mergedfile.pdf
```

from [here](https://www.maketecheasier.com/combine-multiple-pdf-files-with-pdftk/)

## Merge using ghostscript:

```bash
gs -q -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=merged.pdf simple1.pdf simple2.pdf simple3.pdf
```

from [here](https://www.baeldung.com/linux/merge-pdf-files)

## Shrink a PDF from the command line

```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
```

other compession settings:


* ```/screen```: lowest
* ```/ebook```: medium
* ```/printer```: high
* ```/prepress```: very high
* ```/default```: balanced


## Convert to PDF-A

```bash
gs -dPDFA -dBATCH -dNOPAUSE -sColorConversionStrategy=UseDeviceIndependentColor -sDEVICE=pdfwrite -dPDFACompatibilityPolicy=2 -sOutputFile="outputfile.pdf" "inputfile.pdf"
```