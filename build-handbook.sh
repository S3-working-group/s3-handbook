# prepare handbook build
python _python/prepare_handbook.py

if [ "$?" != "0" ]; then
	echo "---error while preparing handbook! --" 1>&2
	exit 1
fi

# transclude all to one file 
multimarkdown --to=mmd --output=handbook/handbook-compiled.md handbook/handbook--master.md
multimarkdown --to=mmd --output=handbook/handbook-epub-compiled.md handbook/handbook-epub--master.md


multimarkdown --to=latex --output=handbook/handbook-compiled.tex handbook/handbook-compiled.md
cd handbook
latexmk -pdf master.tex 
mv master.pdf ../S3-patterns-handbook.pdf
# clean up
latexmk -C
pandoc handbook-epub-compiled.md -f markdown -t epub3 -s -o ../S3-patterns-handbook.epub