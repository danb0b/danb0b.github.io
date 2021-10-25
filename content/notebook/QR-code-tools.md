---
title: QR Code Tools
---

from [here](https://linuxcommando.blogspot.com/2020/07/how-to-generate-and-read-qr-code-on.html)

```bash
sudo apt install qrencode zbar-tools 
```

```bash
qrencode -o webURL.png  'https://linuxcommando.blogspot.com/'
```

```bash
zbarimg webURL.png
```
