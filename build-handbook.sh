# prepare handbook build
python _python/prepare_handbook.py

# transclude all to one file 
multimarkdown --to=mmd --output=handbook/handbook-compiled.md handbook/handbook--master.md
multimarkdown --to=latex --output=handbook/handbook-compiled.tex handbook/handbook-compiled.md
cd handbook
latexmk -pdf master.tex 
# clean up
latexmk -C
