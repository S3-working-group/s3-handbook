# prepare handbook build
python _python/prepare_handbook.py

# transclude all to one file 
multimarkdown --to=mmd --output=handbook/handbook-full.md handbook/handbook--master.md
