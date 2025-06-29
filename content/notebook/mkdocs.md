---
title: mkdocs info
tags:
- websites
- markdown
- mkdocs
summary: " "
---

## Python environment

```bash
sudo apt install -y git python3-pip python3-venv
python3 -m venv ~/envs/mkdocs
. envs/mkdocs/bin/activate
pip install \
mkdocs \
mkdocs-material \
mkdocs-glightbox \
mkdocs-material-extensions \
mkdocs-rss-plugin
```

## External Resources

* <https://stackoverflow.com/questions/27882261/mkdocs-and-mathjax>
* <https://www.mkdocs.org/user-guide/writing-your-docs/>
* <https://squidfunk.github.io/mkdocs-material/>
* <https://www.markdownguide.org/tools/mkdocs/>
* <https://facelessuser.github.io/pymdown-extensions/extensions/>

load mathjax at the beginning:

* <https://stackoverflow.com/questions/61832890/how-to-add-script-to-head-tag-in-mkdocs>

strikethrough support:

```bash
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

