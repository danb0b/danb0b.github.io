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

  > do not allow bitwarden in private tabs

* zotero

## Ublock origin

add the following to block google login popup

```text
||id.google.com^
||accounts.google.com/gsi/*
||smartlock.google.com^
docs.google.com##.modal-dialog
```



## Configure flatseal for userspace

## Bitwarden

1. install [bitwarden plugin](https://bitwarden.com/download/) for firefox.
1. sign in

## External Resources

* Ublock origin config
    * <https://support.mozilla.org/en-US/questions/1393427>
    * <https://techpp.com/2024/05/28/disable-sign-in-with-google-on-websites/>
    <https://stackoverflow.com/questions/69004177/blocking-sign-in-with-google-iframes-using-ublock-origin>