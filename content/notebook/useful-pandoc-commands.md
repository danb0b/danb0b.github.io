---
title: Useful Pandoc Commands
weight: 99
tags:
  - pandoc
  - bash
summary: " "
---

## Get Current Templates

```bash
pandoc --print-default-template=markdown > pandoc-template.md
```

```bash
pandoc --print-default-template=latex>pandoc-template.tex
```

## simple markdown to pdf

```bash
pandoc input-file.md -s -t latex+smart --citeproc --pdf-engine=xelatex --no-highlight -o output-file.pdf
```

### header

See [variables for latex](https://pandoc.org/MANUAL.html#variables-for-latex) and [metadata variables](https://pandoc.org/MANUAL.html#metadata-variables) for all variables.

```bash
summary: " "
---
title: Syllabus for Foldable Robotics 
subtitle: Version 2020-12-31
author: Daniel M. Aukes
date: Spring 2021
published: false
mainfont: Roboto
sansfont: Roboto
geometry: margin=1in
summary: " "
---
```

## Reference docs

```bash
pandoc -o custom-reference.docx --print-default-data-file reference.docx
pandoc -o custom-reference.odt --print-default-data-file reference.odt
```

## Code Highlighting

pandoc does not implement revealjs themes, but there is information about it here:

<https://revealjs.com/code/>



https://highlightjs.org/demo


```bash
pandoc --list-highlight-languages
pandoc --list-highlight-styles
pandoc --print-highlight-style pygments > my.theme
pandoc --highlight-style my.theme
```

To disable highlighting, use the ```--no-highlight``` option.

<https://pandoc.org/chunkedhtml-demo/13-syntax-highlighting.html>
<https://pygments.org/docs/styles/>

## External links

### Automation

* <https://github.com/maehr/academic-pandoc-template>

### Creating books

* <https://medium.com/@sydasif78/book-creation-with-pandoc-and-markdown-893c7d72cb35>
* <https://github.com/sydasif/my-pandoc-book>
* <https://learnbyexample.github.io/customizing-pandoc/>
* <https://www.thepolyglotdeveloper.com/2019/10/creating-ebook-pandoc-markdown/>
* <https://scastiel.dev/how-i-use-pandoc-to-create-my-programming-ebooks>
