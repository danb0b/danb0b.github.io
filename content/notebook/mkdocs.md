---
title: mkdocs info
tags:
- websites
- markdown
- mkdocs
summary: ""
---

## External Resources

```bash
pip install mkdocs mkdocs-material mkdocs-glightbox
```

* <https://stackoverflow.com/questions/27882261/mkdocs-and-mathjax>
* <https://www.mkdocs.org/user-guide/writing-your-docs/>
* <https://squidfunk.github.io/mkdocs-material/>
* <https://www.markdownguide.org/tools/mkdocs/>
* <https://facelessuser.github.io/pymdown-extensions/extensions/>

load mathjax at the beginning:

* <https://stackoverflow.com/questions/61832890/how-to-add-script-to-head-tag-in-mkdocs>

strikethrough support:

```
markdown_extensions:
  ...
  - pymdownx.tilde: {}
  ...
```

* <https://facelessuser.github.io/pymdown-extensions/extensions/tilde/>


## New Project

```bash
mkdocs new my-project
cd my-project
```