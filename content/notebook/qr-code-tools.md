---
title: QR Code Tools
weight: 99
tags:
- linux
- ubuntu
- bash
- tools
summary: ""
---

modified from [this site](https://linuxcommando.blogspot.com/2020/07/how-to-generate-and-read-qr-code-on.html)

## Installing

```bash
sudo apt install -y qrencode #encoding tools
sudo apt install -y zbar-tools # decoding tools
sudo apt install -y qtqr #graphical encoder

```

## Terminal

### Encoding

```bash
qrencode -o webURL.png  'https://linuxcommando.blogspot.com/'
```

	


### Decoding

```bash
zbarimg webURL.png
zbarimg -q webURL.png # only output result
zbarimg -v webURL.png #verbose mode
```

## GUI

run qtqr.  the menu system is quite intuitive.
