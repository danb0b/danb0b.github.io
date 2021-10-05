---
title: Useful Pandoc Commands
tags:
  - pandoc
  - bash
---

## Get Current Templates

```
pandoc --print-default-template=markdown > pandoc-template.md
```

```
pandoc --print-default-template=latex>pandoc-template.tex
```
    
    
## simple markdown to pdf

```bash
pandoc input-file.md -s -t latex+smart --citeproc --pdf-engine=xelatex --no-highlight -o output-file.pdf
```

### header

See [variables for latex](https://pandoc.org/MANUAL.html#variables-for-latex) and [metadata variables](https://pandoc.org/MANUAL.html#metadata-variables) for all variables.

```
---
title: Syllabus for Foldable Robotics 
subtitle: Version 2020-12-31
author: Daniel M. Aukes
date: Spring 2021
published: false
mainfont: Roboto
sansfont: Roboto
geometry: margin=1in
---
```