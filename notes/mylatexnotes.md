## My LaTeX Notes

TLDR; Important notes related to LaTeX

### Adding line numbers to documents: [lineno pkg](https://texblog.org/2012/02/08/adding-line-numbers-to-documents/)
```
\usepackage{lineno}
\linenumbers
```

### [Balance last page in two columns paper](http://latex.org/forum/viewtopic.php?t=4226)
```
\documentclass{article}
\usepackage{balance}
 
\begin{document}
blah blah
 
\bibliographystyle{mystyle}
\balance
\bibliography{references}
\end{document}
```
