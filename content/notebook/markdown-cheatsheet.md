---
title: Markdown Cheat Sheet
tags:
- markdown
---

Derived from <https://towardsdatascience.com/the-ultimate-markdown-cheat-sheet-3d3976b31a0>

# Headings

There are few options to create headings. We can use Markdown or HTML or an alternative syntax to create our desired headings.

First, let's talk about the markdown syntax.

    # Heading 1
    ## Heading 2
    ### Heading 3
    #### Heading 4
    ##### Heading 5

The second option, using the HTML syntax.

    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <h4>Heading 4</h4>
    <h5>Heading 5</h5>

Finally, we can use an alternate syntax. This method only works for heading 1 and heading 2. Add any number of `=` or `-` below the text for heading 1 or heading 2.

    Heading 1
    =

    Heading 2
    -

Now, let's see how it looks on GitHub.

Heading 1
=

Heading 2
-

# Text styles

Using markdown syntax, we can change texts' styles, including bold, italic, blockquotes, monospaced, underlined, strike-through, boxed, subscript, and superscript.

We can use two asterisks (`**`), underscores (`__`), or an HTML tag `<strong>` to make a text bold. To make text italic, we can use one asterisk (`*`), underscore (`_`), or an HTML tag `<em>`. Also, we can make the text bold and italic at the same time.

Bold

    **The quick brown fox jumps over the lazy dog.**

    __The quick brown fox jumps over the lazy dog.__

    <strong>The quick brown fox jumps over the lazy dog.</strong>

Italic

    *The quick brown fox jumps over the lazy dog.*

    _The quick brown fox jumps over the lazy dog._

    <em>The quick brown fox jumps over the lazy dog.</em>

Bold and Italic

    **_The quick brown fox jumps over the lazy dog._**

    <strong><em>The quick brown fox jumps over the lazy dog.</em></strong>


Now, let's see how it looks on GitHub.

Bold

**The quick brown fox jumps over the lazy dog.**

__The quick brown fox jumps over the lazy dog.__

<strong>The quick brown fox jumps over the lazy dog.</strong>

Italic

*The quick brown fox jumps over the lazy dog.*

_The quick brown fox jumps over the lazy dog._

<em>The quick brown fox jumps over the lazy dog.</em>

Bold and Italic

**_The quick brown fox jumps over the lazy dog._**

<strong><em>The quick brown fox jumps over the lazy dog.</em></strong>


To create blockquote, we can use the greater than sign `>`. We can create a single-line or multi-line blockquote. Also, blockquote inside a blockquote. We can add other text styles inside a blockquote, such as bold or italic text styles.

    Blockquotes
    > The quick brown fox jumps over the lazy dog.> The quick brown fox jumps over the lazy dog.
    >
    > The quick brown fox jumps over the lazy dog.
    >
    > The quick brown fox jumps over the lazy dog.> The quick brown fox jumps over the lazy dog.
    >> The quick brown fox jumps over the lazy dog.
    >>> The quick brown fox jumps over the lazy dog.> **The quick brown fox** *jumps over the lazy dog.*

Now, let's see how it looks on GitHub.

> The quick brown fox jumps over the lazy dog.> The quick brown fox jumps over the lazy dog.
>
> The quick brown fox jumps over the lazy dog.
>
> The quick brown fox jumps over the lazy dog.> The quick brown fox jumps over the lazy dog.
>> The quick brown fox jumps over the lazy dog.
>>> The quick brown fox jumps over the lazy dog.> **The quick brown fox** *jumps over the lazy dog.*

We can achieve monospaced, and underlined styles using HTML tags `<samp>` and `<ins>`. For a strike-through style, we can use two tilda sign `~~`.

    Monospaced: <samp>The quick brown fox jumps over the lazy dog.</samp>

    Underlined: <ins>The quick brown fox jumps over the lazy dog.</ins>

    Strike-through: ~~The quick brown fox jumps over the lazy dog.~~

Now, let's see how it looks on GitHub.

Monospaced: <samp>The quick brown fox jumps over the lazy dog.</samp>

Underlined: <ins>The quick brown fox jumps over the lazy dog.</ins>

Strike-through: ~~The quick brown fox jumps over the lazy dog.~~

We can use an HTML `<table>` tag to create a box.

    Boxed
    <table><tr><td>The quick brown fox jumps over the lazy dog.</td></tr></table>

Now, let's see how it looks on GitHub.

<table><tr><td>The quick brown fox jumps over the lazy dog.</td></tr></table>

We can achieve subscript and superscript styles using HTML tag `<sub>` and `<sup>`. It is useful when you're writing a mathematical formula.

    Subscript: <sub>The quick brown fox jumps over the lazy dog.</sub>

    Superscript: <sup>The quick brown fox jumps over the lazy dog.</sup>

Now, let's see how it looks on GitHub.

Subscript: <sub>The quick brown fox jumps over the lazy dog.</sub>

Superscript: <sup>The quick brown fox jumps over the lazy dog.</sup>

# Syntax Highlighting

We can use a single backtick `` ` `` before and after the code block to create the following view.

    A class method is an instance method of the class object. When a new class is created, an object of type `Class` is initialized and assigned to a global constant (Mobile in this case).

As you can see the word **Class** is highlighted.

![Code Highlighting]

We can also use triple backticks ```` ``` ```` before and after the code block to create the following view.

    ```
    public static String monthNames[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};```

![Code Highlighting][5]

We can add an optional language identifier to enable syntax highlighting. Refer to this [GitHub] document to find all the valid keywords.

    ```java
    public static String monthNames[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};```

Now, let's see how it looks on GitHub.

![Syntax Highlighting]

# Alignments

By using HTML tags, we can align README contents.

    <p align="left">
    <img src="https://images.unsplash.com/photo-1415604934674-561df9abf539?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2772&q=80" width="100" height="100" border="10"/>
    </p>

    <p align="center">
    <img src="https://images.unsplash.com/photo-1415604934674-561df9abf539?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2772&q=80" width="100" height="100" border="10"/>
    </p>

![Center align]

    <p align="right">
    <img src="https://images.unsplash.com/photo-1415604934674-561df9abf539?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2772&q=80" width="100" height="100" border="10"/>
    </p>

![Right align]

Now, let's align a text.

    <h3 align="center"> My latest Medium posts </h3>

![Center align][6]

# Tables

Let's create a table without headers.

    <table>
    <tr>
    <td width=”33%””>
    The quick brown fox jumps over the lazy dog.
    </td>
    <td width=”33%”>
    The quick brown fox jumps over the lazy dog.
    </td>
    <td width=”33%”>
    The quick brown fox jumps over the lazy dog.
    </td>
    </tr>
    </table>

![Table without header]

To create a table with headers we need to use dashes to separate each header cell and use pipes to separate columns. The outer pipes are optional. We can use any number of dashes and spaces to increase readability. We can use colons to align columns. For left-align text, use a colon to the left of dashes. For center-align text, use a colon on both sides of dashes. For right-align text, use a colon to the right of dashes. By default Left align is used.

    | Default | Left align | Center align | Right align |
    | - | :- | :-: | -: |
    | 9999999999 | 9999999999 | 9999999999 | 9999999999 |
    | 999999999 | 999999999 | 999999999 | 999999999 |
    | 99999999 | 99999999 | 99999999 | 99999999 |
    | 9999999 | 9999999 | 9999999 | 9999999 || Default    | Left align | Center align | Right align |
    | ---------- | :--------- | :----------: | ----------: |
    | 9999999999 | 9999999999 | 9999999999   | 9999999999  |
    | 999999999  | 999999999  | 999999999    | 999999999   |
    | 99999999   | 99999999   | 99999999     | 99999999    |
| 9999999    | 9999999    |  9999999   | 9999999     |Default    | Left align | Center align | Right align |
|:-----------|:-----------|:----------:|------------------------------------------------------------------:|
| 9999999999 | 9999999999 | 9999999999 |                                                        9999999999 |
| 999999999  | 999999999  | 999999999  |                                                         999999999 |
| 99999999   | 99999999   |  99999999  |                                                          99999999 |
| 9999999    | 9999999    |  9999999   |                                                           9999999 |

![Table with different alignments]

Now display two tables side by side.

    <table>
    <tr>
    <th>Heading 1</th>
    <th>Heading 2</th>
    </tr>
    <tr>

    <td>

    | A | B | C |
    |--|--|--|
    | 1 | 2 | 3 |

    </td><td>

    | A | B | C |
    |--|--|--|
    | 1 | 2 | 3 |

    </td></tr> </table>

![Display two tables side by side]

Let's create a table with multiple lines using the HTML `<br/>` tag.

    | A | B | C |
    |---|---|---|
    | 1 | 2 | 3 <br/> 4 <br/> 5 |

![A table with multiple lines]

# Links

We can create a link in four ways. The first one is by using an inline style. The second one uses reference style, the third one using relative links, and finally auto links.

    [The-Ultimate-Markdown-Cheat-Sheet (https://github.com/lifeparticle/The-Ultimate-Markdown-Cheat-Sheet)

![Inline-style]

If you're using the same link more the once, then using the reference style would be beneficial since you don't have to write the link every time, and also, it's easy to update the link. Moreover, you can use numbers for the reference text. Also, you can use the reference text as the link text.

    [The-Ultimate-Markdown-Cheat-Sheet][reference text][The-Ultimate-Markdown-Cheat-Sheet][1][Markdown-Cheat-Sheet][reference text]: https://github.com/lifeparticle/The-Ultimate-Markdown-Cheat-Sheet
    [1]: https://github.com/lifeparticle/The-Ultimate-Markdown-Cheat-Sheet
    [Markdown-Cheat-Sheet]: https://github.com/lifeparticle/The-Ultimate-Markdown-Cheat-Sheet

![Three variations of reference-style]

We can also create relative links with all relative link operands, such as `./` and `../`.

    [Example of a relative link](rl.md)

![Example of a relative link]

GitHub can automatically create links from standard URLs.

    Visit https://github.com/

![Auto link]

# Images {#f407 .lx .ls .gq .bf .ly .lz .ma .kb .mb .mc .md .ke .me .mf .mg .mh .mi .mj .mk .ml .mm .mn .mo .mp .mq .mr .hn selectable-paragraph=""}

We can add images using the similar techniques we used for links.

    ![alt text](https://images.unsplash.com/photo-1415604934674-561df9abf539?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=100&q=80)

![Inline-style][7]

    ![alt text][image][image]: https://images.unsplash.com/photo-1415604934674-561df9abf539?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=100&q=80

![Reference-style]

Also, we can use the HTML `img` tag to add an image.

    <img src="https://images.unsplash.com/photo-1415604934674-561df9abf539?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2772&q=80" width="100" height="100" border="10"/>

![img tag]

We can also embed GIF and SVG.

    <img src="https://media.giphy.com/media/qLHzYjlA2FW8g/giphy.gif" />

![GIF]

    <img src="https://img.shields.io/badge/theultimatemarkdowncheatsheet-brightgreen.svg" />

![SVG]

# Lists

For lists, we can have ordered and unordered lists.

    1. One
    2. Two
    3. Three

![An ordered list]

Now let's create an ordered list with sub-items.

    1. First level
        1. Second level
            - Third level
                - Fourth level
    2. First level
        1. Second level
    3. First level
        1. Second level

![An ordered list with sub-items]

To create an unordered list, we can asterisk, plus, or minus sign.

    * 1
    * 2
    * 3+ 1
    + 2
    + 3- 1
    - 2
    - 3

![Unordered lists]

Now let's create an unordered list with sub-items.

    - First level
        - Second level
            - Third level
                - Fourth level
    - First level
        - Second level
    - First level
        - Second level

![An unordered list with sub-items]

We can also use HTML to create a list.

    <ul>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
    <li>Fourth item</li>
    </ul>

![A list using HTML]

Now let's create a task list. We can create a task list using a hyphen followed by `[ ]`, and to mark a task complete, put an `x` inside the brackets.

    - [x] Fix Bug 223
    - [ ] Add Feature 33
    - [ ] Add unit tests

![Tasklist]

# Horizontal Rule

We can use three hyphens, asterisks, or underscores to create a horizontal line.

    ---
    ***
    ___

![Horizontal Rule]

# Miscellaneous

We can include comments inside a `.md` file.

    <!--
    Lorem ipsum dolor sit amet
    -->

We can use a backslash to escape literal characters. Before escaping.

    *   Asterisk
    \   Backslash
    `   Backtick
    {}  Curly braces
    .   Dot
    !   Exclamation mark
    #   Hash symbol
    -   Hyphen symbol
    ()  Parentheses
    +   Plus symbol
    []  Square brackets
    _   Underscore

![Before escaping]

After escaping.

    \*   Asterisk
    \\   Backslash
    \`   Backtick
    \{}  Curly braces
    \.   Dot
    \!   Exclamation mark
    \#   Hash symbol
    \-   Hyphen symbol
    \()  Parentheses
    \+   Plus symbol
    \[]  Square brackets
    \_   Underscore

![After escaping]

We can also include [emojis] in our `.md` file.

    :octocat:

![An octocat emoji]

We can mention a person or team by typing `@` with their username or team name.

    @lifeparticle

![Mention a person]

We can also bring up a list of suggested issues and pull requests within the repository by typing `#`.

    #

# Tools

There are various tools for Markdown, which will help you to build a beautiful GitHub README faster.

1.  Create a Markdown table of content --- [GitHub][8]
2.  Create an empty Markdown table --- [Tablesgenerator]
3.  Convert Excel to Markdown table --- [Tableconvert]
4.  Markdown preview for Sublime Text 3 --- [Packagecontrol]
5.  Markdown preview Visual Studio Code --- [Marketplace]

Congratulation! Now you know how to create an awesome README for your next project. I hope you learned something new. Now have a look into the official documentation on [GitHub][9]. Happy coding!


  [Headings]: markdown-cheatsheet_files/1R5zPdVT4YGzOEOfMfgDyFg_005.png
  [1]: markdown-cheatsheet_files/1ZBjm6J3bli0yiNCzB2YDkA.png
  [2]: markdown-cheatsheet_files/1TCcBjdADcPVDPHRlr0N_Gw.png
  [Bold and Italic text styles]: markdown-cheatsheet_files/12vxP5Bzx-Pfh4ObWUQtqCA.png
  [Blockquotes text styles]: markdown-cheatsheet_files/1FBzb8H_BevCHQArac0kjTg.png
  [3]: markdown-cheatsheet_files/1OEwoTS8Tiz7JiH02plAzQw.png
  [4]: markdown-cheatsheet_files/1RaAcDEZB_MgI_OOqpVJ0aA.png
  [Monospaced, Underlined, and Strike-through text styles]: markdown-cheatsheet_files/1o9_MQR5rD2BJxotap4rJsg.png
  [Boxed text style]: markdown-cheatsheet_files/1SlUzlZcnaWa9ohqKCEiOwQ_003.png
  [Subscript and Superscript text styles]: markdown-cheatsheet_files/1Cc2ApjvtP9aVHgpeTnox-g_002.png
  [Code Highlighting]: markdown-cheatsheet_files/1-CHOJJ4q_VnzELliMgSLzg_004.png
  [5]: markdown-cheatsheet_files/1csK2zdkIvJqeoRP9wm5_pg_003.png
  [GitHub]: https://github.com/github/linguist/blob/master/lib/linguist/languages.yml
  [Syntax Highlighting]: markdown-cheatsheet_files/1fGruR9hQN8Wx9ufiAbWr2w_002.png
  [Center align]: markdown-cheatsheet_files/1oA1Ubn8Cq2WNogelJjot0Q.png
  [Right align]: markdown-cheatsheet_files/1mIhPg9ni0xn2nSsRJ5ghMA.png
  [6]: markdown-cheatsheet_files/1pTwjTZhxZJsaH-j6ved0Hw.png
  [Table without header]: markdown-cheatsheet_files/1SREVUDKD5qj4zd4FdTVdZQ_002.png
  [Table with different alignments]: markdown-cheatsheet_files/1TK857IrYsP-eTnN015kAyw_002.png
  [Display two tables side by side]: markdown-cheatsheet_files/1XbjjJ36RMHn0nM6MEqpejA_002.png
  [A table with multiple lines]: markdown-cheatsheet_files/15jnkkps0EYyC4SqJWBFRVA.png
  [Inline-style]: markdown-cheatsheet_files/1raqS3fp8uvbvB4uKhe0s6w_002.png
  [Three variations of reference-style]: markdown-cheatsheet_files/1ROuRegTM5icevNnARf1JCw.png
  [Example of a relative link]: markdown-cheatsheet_files/1s9TynxAl1HtIgz-DtSdUug_002.png
  [Auto link]: markdown-cheatsheet_files/1Xp_MqrN-_VfFKYzCF_iYVQ_002.png
  [7]: markdown-cheatsheet_files/1atPl5Vz8yZkEBhU1714kpw_002.png
  [Reference-style]: markdown-cheatsheet_files/16ZjAngXhioPsKjX3I6y8Nw.png
  [img tag]: markdown-cheatsheet_files/1cmSy9pNbX-5s5Xwt2IMfUQ.png
  [GIF]: markdown-cheatsheet_files/1ZwWQGxyA3JwEESgY4cFivg.gif
  [SVG]: markdown-cheatsheet_files/1KEE8BR5oz4aXYV8s-2Jyag_002.png
  [An ordered list]: markdown-cheatsheet_files/103HieQqdi5RcmEB8XOQbTw_002.png
  [An ordered list with sub-items]: markdown-cheatsheet_files/1xKyDR_4pYOuWxjGb6wjuIg.png
  [Unordered lists]: markdown-cheatsheet_files/1CfnDlPWggDU3Q40DxPhOPw_002.png
  [An unordered list with sub-items]: markdown-cheatsheet_files/1KzLWxNhfGxUjLp0La6mgfA.png
  [A list using HTML]: markdown-cheatsheet_files/1w_sG84PZOeT1FkkZdlKU3A_002.png
  [Tasklist]: markdown-cheatsheet_files/1QQ3D9_pki5eHqoVrXyQ7Pg_003.png
  [Horizontal Rule]: markdown-cheatsheet_files/1RSIIn3j3SJ5SvwrwJ0dvvQ_004.png
  [Before escaping]: markdown-cheatsheet_files/1dJaMNAnGwrsXrCiRQWmqbw.png
  [After escaping]: markdown-cheatsheet_files/1uy9GOaQqDUUl03LylcQ7Vg_005.png
  [emojis]: https://gist.github.com/rxaviers/7360908
  [An octocat emoji]: markdown-cheatsheet_files/1dROV-F6NHea-wNC96WjYog.png
  [Mention a person]: markdown-cheatsheet_files/1U1QXcuh80vcyDhDHvF6Ipg_005.png
  [8]: https://github.com/ekalinin/github-markdown-toc
  [Tablesgenerator]: https://www.tablesgenerator.com/markdown_tables
  [Tableconvert]: https://tableconvert.com/
  [Packagecontrol]: https://packagecontrol.io/packages/MarkdownPreview
  [Marketplace]: https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced
  [9]: https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax
