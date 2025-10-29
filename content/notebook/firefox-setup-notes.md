---
title: Firefox Setup Notes
---


## about:config

go to ```about:config```

turn off AI features

```text
browser.ml.linkPreview.enabled
browser.ml.chat.enabled
browser.ml.enable
browser.tabs.groups.smart.enabled
browser.tabs.groups.smart.userEnabled
extensions.ml.enabled
sidebar.revamp
```

turn on global privacy control:

```text
privacy.globalprivacycontrol.enabled
```

set ```media.autoplay.default``` to 2

disable pocket:

```
extensions.pocket.enabled 
```

turn on graphics rendering

```
gfx.webrender.all
```

disable automatic refresh

```browser.meta_refresh_when_inactive.disabled```

fingerprinting isolation: set these to true

```privacy.resistFingerprinting```: breaks time in gmail
```privacy.firstparty.isolate```
```privacy.trackingprotection.fingerprinting.enabled```
```privacy.trackingprotection.cryptomining.enabled```

```browser.send_pings```: set to false

turn off rtc:

```media.peerconnection.enabled```

```beacon.enabled```: set to false

```privacy.bounceTrackingProtection.mode```: set to 1

```network.cookie.cookieBehavior```: set to 5

```dom.event.clipboardevents.enabled```: false-- breaks google drive copy/paste

```browser.sessionstore.privacy_level```: set to 2

```privacy.userContext.longPressBehavior``` set to 2.

```browser.urlbar.speculativeConnect.enabled```: set to false

```cookiebanners.service.mode.privateBrowsing``` set to 1

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
* about:config
    * <https://www.howtogeek.com/firefox-config-setting-tweaks-improved-performance-privacy-and-more/>
    * <https://umatechnology.org/most-useful-mozilla-firefox-aboutconfig-tweaks/>
    * <https://avoidthehack.com/firefox-privacy-config>
