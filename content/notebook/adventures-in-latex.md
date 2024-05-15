---
title: Adventures in Latex
---

https://tex.stackexchange.com/questions/1137/where-do-i-place-my-own-sty-or-cls-files-to-make-them-available-to-all-my-te
https://tex.stackexchange.com/questions/20160/how-to-register-my-own-packages-or-classes-in-a-separate-drive-to-tex-live-insta
https://tex.stackexchange.com/questions/120150/is-there-a-difference-between-texconfig-rehash-and-mktexlsr
https://www.overleaf.com/learn/latex/Articles/An_introduction_to_Kpathsea_and_how_TeX_engines_search_for_files
https://tug.org/texinfohtml/kpathsea.html#Path-searching
https://tex.stackexchange.com/questions/1137/where-do-i-place-my-own-sty-or-cls-files-to-make-them-available-to-all-my-te

```bash
texhash --help
texhash --verbose
nano test.md
pandoc-plus test.md -o pdf -t default
pandoc-plus test.md -o pdf -t letter
echo $HOME
texhash $HOME/repos/code/code_pandoc_plus/texmf/
texhash $HOME/repos/code/code_pandoc_plus/texmf
texhash --verbose
texhash --verbose $HOME/repos/code/code_pandoc_plus/texmf
pandoc-plus test.md -o pdf -t letter
pandoc -s -t latex+smart --citeproc --data-dir=/home/danaukes/repos/code/code_pandoc_plus/pandoc --template=letter.tex --pdf-engine=xelatex --wrap=none --reference-links -o "test.pdf" "test.md"
texhash --verbose
texhash --verbose $HOME/repos/code/code_pandoc_plus/texmf
texhash --verbose $HOME/repos/code/code_pandoc_plus/texmf/tex
pandoc -s -t latex+smart --citeproc --data-dir=/home/danaukes/repos/code/code_pandoc_plus/pandoc --template=letter.tex --pdf-engine=xelatex --wrap=none --reference-links -o "test.pdf" "test.md"
texconfig --help
texconfig rehash
sudo texhash --verbose $HOME/repos/code/code_pandoc_plus/texmf/tex
sudo texhash --verbose $HOME/repos/code/code_pandoc_plus/texmf
pandoc -s -t latex+smart --citeproc --data-dir=/home/danaukes/repos/code/code_pandoc_plus/pandoc --template=letter.tex --pdf-engine=xelatex --wrap=none --reference-links -o "test.pdf" "test.md"
pandoc -s -t latex+smart --citeproc --data-dir=/home/danaukes/repos/code/code_pandoc_plus/pandoc --template=letter.tex  --wrap=none --reference-links -o "test.pdf" "test.md"
kpsewhich -var-value=TEXMFHOME
kpsewhich pandoc.sty
kpsewhich --help
kpsewhich -help
kpsewhich -help-formats
kpsewhich -help-formats | grep .sty
kpsewhich -help-formats | grep sty
kpsewhich -show-path=TEXINPUTS
kpsewhich -show-path=.sty
kpsewhich -help
kpsewhich -show-path
kpsewhich -show-path=.tex
man kpsewhich
echo $TEXMFHOME
kpsewhich -var-value=TEXMFHOME
echo $TEXMF
kpsewhich -var-value=TEXMF
kpsewhich -var-value=TEXMFDBS
echo $TEXINPUTS
export $TEXINPUTS=/home/danaukes/repos/code/code_pandoc_plus/texmf
export "$TEXINPUTS=/home/danaukes/repos/code/code_pandoc_plus/texmf"
export TEXINPUTS=/home/danaukes/repos/code/code_pandoc_plus/texmf
echo $TEXINPUTS 
kpsewhich -var-value=TEXMFDBS
kpsewhich -var-value=TEXMFc
kpsewhich -show-path=.tex
exit
kpsewhich -show-path=.tex
kpsewhich -show-path=TEXINPUTS
kpsewhich -var-value=TEXMFHOME
export "$TEXINPUTS=/home/danaukes/repos/code/code_pandoc_plus/texmf"
export TEXINPUTS=/home/danaukes/repos/code/code_pandoc_plus/texmf
pp-beamer test.md  -o pdf -t letter
pandoc /home/danaukes/repos/code/code_pandoc_plus/bat/beamer_default.yaml -V titlegraphic="/home/danaukes/repos/code/code_pandoc_plus/support/fulton.png" -s -t beamer --pdf-engine=xelatex --slide-level=2 -o "test.pdf" "test.md"
tail -200 .bash_history
kpeswhich -help
kpsewhich -help
kpsewhich -a texmf.cnf
nano /etc/texmf/web2c/texmf.cnf 
cd /etc/texmf/
ls
cd texmf.d/
ls
cat 00debian.cnf 
cd ../tex
ls
cd generic/
ls
cd config/
ls
ls -la
kpsewhich -var-value=VARTEXFONTS
kpsewhich -show-path=cnf
kpsewhich -show-path=tx
kpsewhich -show-path=tex
kpsewhich -show-path=sty
kpsewhich -show-path=tex
exit
kpsewhich -var-value=TEXMFDBS
kpsewhich -var-value=TEXMF
exit
danaukes@zenbook:~$ 

```


% or create an additional one (with the extension '.cnf'),
% and invoke update-texmf.

export TEXINPUTS="$HOME/repos/code/code_pandoc_plus/python/pandoc_plus/support/texmf//:"

