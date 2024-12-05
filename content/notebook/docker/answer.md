---
title: Answer on Docker
tags:
- answer
- docker
- ubuntu
- mariadb
summary: " "
---

replace ```<password1>``` with your own password

```yaml
version: "3"
services:
  answer:
    image: answerdev/answer
    ports:
      - '9080:80'
    restart: on-failure
    volumes:
      - answer-data:/data
    depends_on:
      - mariadb      

  mariadb:
    restart: unless-stopped
    image: mariadb:10.10
    security_opt: 
      - seccomp:unconfined
      - apparmor:unconfined
    command: mysqld --innodb-buffer-pool-size=512M --transaction-isolation=READ-COMMITTED --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --max-connections=512 --innodb-rollback-on-timeout=OFF --innodb-lock-wait-timeout=120
    volumes:
      - "./database:/var/lib/mysql"
    ports:
      - "33061:3306"
    environment:
      MARIADB_AUTO_UPGRADE: "1"
      MARIADB_INITDB_SKIP_TZINFO: "1"
      MARIADB_DATABASE: "answer"
      MARIADB_ROOT_USER: "answer"
      MARIADB_ROOT_PASSWORD: <password1>
      MARIADB_USER: "answer"
      MARIADB_PASSWORD: <password1>

volumes:
  answer-data:
```