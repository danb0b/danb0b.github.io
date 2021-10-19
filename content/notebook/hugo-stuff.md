---
title: Hugo Stuff
tags:
  - markdown
  - hugo
  - websites
---

## Install

Make sure you install add-ons

## Create a new site with yaml format

Modified from [here](https://gohugo.io/getting-started/quick-start/)

1. Create directory Structure

    ```bash
    hugo new site --format=yaml foldername
    cd foldername
    ```

1. Initialize ```git``` repository and add theme

    Might I suggest using [this forked version](https://github.com/danb0b/external_liva-hugo) of the "liva" theme?  It has some nice enhancements

    ```bash
    git init
    git submodule add https://github.com/danb0b/external_liva-hugo.git themes/liva-hugo
    ```
    
1. Add theme to ```config.yaml```

    ```bash
    echo theme: \"liva-hugo\" >> config.yaml
    ```

1. Customize ```config.yaml```

1. Run server for testing

    Production:

    ```bash
    hugo server
    ```

    With Drafts:

    ```bash
    hugo server -D
    ```

1 Build Pages

    Production:

    ```bash
    hugo
    ```

    With drafts:

    ```bash
    hugo -D
    ```

## External Links

### General
* <https://gohugo.io/getting-started/quick-start/>

### Essential Add-ons
* Original [liva theme](https://github.com/gethugothemes/liva-hugo)
* [Citations for Hugo](https://github.com/loup-brun/hugo-cite)
* [custom pagination](https://glennmccomb.com/articles/how-to-build-custom-hugo-pagination/)

### Using with Github Actions
* [automated deploytment on github pages](https://medium.com/@asishrs/automate-your-github-pages-deployment-using-hugo-and-actions-518b959a51f9)
* [detailed setup](https://github.com/peaceiris/actions-hugo)
* [actions-gh-pages](https://github.com/peaceiris/actions-gh-pages#getting-started)

### Themes and Examples
* <https://themes.gohugo.io/hugo-theme-bootstrap4-blog/>
* <https://www.liwen.id.au/photoswipe/>

