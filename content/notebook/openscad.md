---
title: quick scripts for openscad
tags:
- bash
- flatpak
- openscad
- cad
- scripting
---

```bash
color("red",1) import("path/to/your-part.stl");
```



```bash
flatpak run org.openscad.OpenSCAD  -o test.png --projection orthogonal test.scad
```

with camera orientation but no scaling

```bash
flatpak run org.openscad.OpenSCAD  -o test.png --autocenter --viewall --camera 0,0,0,-30,60,0,1000 --projection orthogonal test.scad
```

