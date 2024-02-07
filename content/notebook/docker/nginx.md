---
title: NginX docker config
tags:
- docker
- nginx
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