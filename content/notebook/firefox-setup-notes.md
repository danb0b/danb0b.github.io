---
title: Firefox Setup Notes
---


## Start Pages

Separate by |

## File Preferences

* pdf - save to file

## Cookies

## Add-Ons

* multi account containers
* ublock origin
* privacy badger
* bitwarden
* zotero

do not allow in private tabs

## Ublock origin

add the following to block google login popup

```text
||id.google.com^
||accounts.google.com/gsi/$3p
||smartlock.google.com^
```

from here: <https://support.mozilla.org/en-US/questions/1393427>

### alternative

```text
||accounts.google.com/gsi/*$xhr,script,3p
```

this one suggests differently:

<https://techpp.com/2024/05/28/disable-sign-in-with-google-on-websites/>

More generally:

```text
||accounts.google.com/gsi/*
```

<https://stackoverflow.com/questions/69004177/blocking-sign-in-with-google-iframes-using-ublock-origin>
