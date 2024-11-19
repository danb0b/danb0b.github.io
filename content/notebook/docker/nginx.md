---
title: NginX docker config
tags:
- docker
- nginx
summary: ""
---

docker compose:

```yaml
version: "3.9"
services:
  test:
    image: nginx:latest
    ports:
      - 8080:80
    volumes:
      - ./html:/usr/share/nginx/html
```

## Folder Structure

```txt
.
├── docker-compose.yml
├── html
│   └── index.html
```

Html

```html
Hello, I'm Dan, at  <a href='https://danaukes.com/'>danaukes.com</a>
```


## External Resources

* <https://awstip.com/creating-a-simple-web-server-with-docker-a-step-by-step-guide-to-running-your-web-server-as-a-2992ce2051e3>
