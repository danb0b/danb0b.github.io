---
title: QR Code Tools
---

modified from [this site](https://linuxcommando.blogspot.com/2020/07/how-to-generate-and-read-qr-code-on.html)

## Installing

```bash
sudo apt install qrencode zbar-tools 
```

## Encoding

```bash
qrencode -o webURL.png  'https://linuxcommando.blogspot.com/'
```

## Decoding

```bash
zbarimg webURL.png
zbarimg -q webURL.png # only output result
zbarimg -v webURL.png #verbose mode
```
