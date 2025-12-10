---
title: Mkdocs environment
---

Installs a specific flavor of mkdocs that matches github

```bash
python -m venv ~/envs/mkdocs
. ~/envs/mkdocs/bin/activate
pip install \
mkdocs == 1.5.3 \
mkdocs-glightbox == 0.4.0 \
mkdocs-material == 9.5.18 \
mkdocs-material-extensions == 1.3.1 \
mkdocs-rss-plugin
```