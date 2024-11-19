---
title: Get download with wget and xpath
tags:
- ubuntu
- bash
- wget
- xpath
summary: ""
---


```bash
sudo apt intstall libxml2-utils
```

1. go to firefox and go to the url you want to download something from.

```bash
url="https://www.mendeley.com/download-reference-manager/linux"
echo $url
html=$(wget -q -O - "$url")
```

1. go to firefox, click on the link you want to inspect, right click on "inspect"
1. in the attributes explorer, navigate to the ```<a href="...">...</a>``` tag, right click and copy the "xpath"
1. use the following command to save it as a variable in terminal:

  ```bash
  #xpath="<your xpath here>"
  # example
  xpath="/html/body/div[2]/section[1]/div[1]/a"
  echo $xpath
  ```

1. in the same terminal window

```
dl_url=$(echo $html | xmllint --html --xpath "string($xpath/@href)" - 2>/dev/null | xargs)
echo $dl_url
```

1. Finally,

```bash
wget "$dl_url"
```

## Full Example

```bash
url="https://www.mendeley.com/download-reference-manager/linux" && \
xpath="/html/body/div[2]/section[1]/div[1]/a"  && \
html=$(wget -q -O - "$url")  && \
dl_url=$(echo $html | xmllint --html --xpath "string($xpath/@href)" - 2>/dev/null | xargs) && \
wget "$dl_url" && \
```
