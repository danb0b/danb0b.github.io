---
title: 09-Install and Configure Atom
weight: 9
tags:
- ubuntu
- linux
- atom
---

1. Install

    ```bash
    wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -
    sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list'
    sudo apt-get update
    sudo apt-get install -y atom
    apm install language-markdown markdown-preview-plus markdown-table-formatter wordcount
    # should already have texlive-full installed...
    sudo apt install latexmk
    apm install language-latex latex pdf-view
    ```

1. Create custom configuration file

    ```
    cat <<EOT >> .atom/config.cson
    "*":
      core:
        disabledPackages: [
          "markdown-preview"
          "markdown-scroll-sync"
          "language-gfm"
          "markdown-writer"
          "busy-signal"
          "intentions"
          "linter"
          "linter-ui-default"
          "linter-markdown"
          "whitespace"
          "autocomplete-atom-api"
          "autocomplete-plus"
          "autocomplete-css"
          "autocomplete-html"
          "autocomplete-snippets"
          "go-to-line"
          "markdown-folding"
          "markdown-table-editor"
        ]
        openEmptyEditorOnStart: false
        packagesWithKeymapsDisabled: [
          "markdown-table-editor"
        ]
        telemetryConsent: "no"
        uriHandlerRegistration: "always"
      editor:
        fontSize: 13
        softWrap: true
      "exception-reporting":
        userId: "10613451-9b64-4617-aaa9-d3c2e1770f35"
      "language-markdown":
        autoIncrementListItems: false
        indentListItems: false
        removeEmptyListItems: false
      latex: {}
      "markdown-preview-plus":
        markdownItConfig:
          blockMathSeparators: [
            "$$"
            "$$"
          ]
          inlineMathSeparators: [
            "$"
            "$"
          ]
          useCheckBoxes: false
          useEmoji: false
          useImsize: false
          useLazyHeaders: false
        mathConfig:
          enableLatexRenderingByDefault: true
          latexRenderer: "HTML-CSS"
        pandocConfig:
          pandocArguments: [
            "--citeproc"
          ]
          pandocCSLFile: "ieee.csl"
          pandocRemoveReferences: false
        previewConfig: {}
        renderer: "pandoc"
        saveConfig:
          saveToPDFOptions:
            pageSize: "Letter"
        syncConfig:
          syncEditorOnPreviewScroll: true
          syncPreviewOnChange: true
          syncPreviewOnEditorScroll: true
      "markdown-table-editor": {}
      "markdown-table-formatter": {}
      "spell-check":
        useLocales: false
      "tidy-markdown":
        runOnSave: false
      welcome:
        showOnStartup: false
      whitespace: {}
    ".md.text":
      editor:
        autoIndent: true
        autoIndentOnPaste: false
    EOT
    ```
1. Current ```styles.less```

    ```
    cat <<EOT >> .atom/styles.less
    /*
     * Your Stylesheet
     *
     * This stylesheet is loaded when Atom starts up and is reloaded automatically
     * when it is changed and saved.
     *
     * Add your own CSS or Less to fully customize Atom.
     * If you are unfamiliar with Less, you can read more about it here:
     * http://lesscss.org
     */


    /*
     * Examples
     * (To see them, uncomment and save)
     */

    // style the background color of the tree view
    .tree-view {
      // background-color: whitesmoke;
    }

    // style the background and foreground colors on the atom-text-editor-element itself
    atom-text-editor {
      // color: white;
      // background-color: hsl(180, 24%, 12%);
    }

    // style UI elements inside atom-text-editor
    atom-text-editor .cursor {
      // border-color: red;
    }

    html[data-markdown-preview-plus-context="live-preview"] body {
      font-size: 12pt;
      background-color: #ddd;
      color: #000;

      strong,h1,h2,h3,h4,h5 {
      color: #000;
      }
      th {
      color: #000;
      }

    }
    EOT
    ```

1. Usage

    * ctrl+shift+m to preview markdown pages
    * ctrl+s updates table formats in markdown
    * ctrl+alt+b to make pdf from latex