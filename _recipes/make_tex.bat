@echo off

for %%X in (*.md) do (

	set fname=%par1:~0,-3%
	
	pandoc %%X -t latex+smart --filter pandoc-fignos --natbib --data-dir="%HOMEDRIVE%%HOMEPATH%\code\templates\pandoc" --template=recipe.tex --pdf-engine=xelatex --wrap=none --reference-links  --no-highlight -o %%X.tex
)