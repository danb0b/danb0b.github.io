when making a new overleaf project:

integrate with github by creating a new repositoiry.

if you are not danaukes, it would be best to let danaukes create the repo in the idealab acct; otherwise, share your repository with github danaukes with write permissions

push to the repository before making significant edits on overleaf

push after making significant edits on overleaf

comment your commit

## Latex 

### Edits

We use latex commands to edit.  For example, 


```tex
\usepackage{ulem} 		
\usepackage{xcolor}
\newcommand{\dma}[1]{{\color{blue}#1}}%comment by Dan
\newcommand{\dl}[1]{{\color{red}#1}}
\newcommand{\tofix}[1]{{\color{yellow}#1}}
```

### Figures and tables

create a command for common abbreviations:

```tex
\newcommand{\sectionref}[1]{Sec.~\ref{#1}}
\newcommand{\chapterref}[1]{Ch.~\ref{#1}}
\newcommand{\figureref}[1]{Fig.~\ref{#1}}
\newcommand{\Figureref}[1]{Fig.~\ref{#1}}
\newcommand{\Equationref}[1]{(\ref{#1})}
```
