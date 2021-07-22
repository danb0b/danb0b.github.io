---
title: Grep Cookbook
tags:
- grep
- bash
- linux
---  

# Grep Cookbook

```bash
grep -Iiran "pCtip" ./
```

A more complex example:

```bash
grep --exclude-dir="**.git**" --exclude-dir="**.ipynb_checkpoint**" --exclude="*.png" --exclude="*.svg" -Iran "pCtip" ./
```