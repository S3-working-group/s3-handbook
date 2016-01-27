# root and patterns index
multimarkdown --to=mmd --output=index.md index--master.md
multimarkdown --to=mmd --output=patterns/index.md patterns/index--master.md

# group indexes
multimarkdown --to=mmd --output=patterns/alignment--index.md patterns/alignment--master.md
multimarkdown --to=mmd --output=patterns/bringing-in-s3-patterns--index.md patterns/bringing-in-s3-patterns--master.md
multimarkdown --to=mmd --output=patterns/building-organizations--index.md patterns/building-organizations--master.md
multimarkdown --to=mmd --output=patterns/coordinating-work--index.md patterns/coordinating-work--master.md
multimarkdown --to=mmd --output=patterns/effective-meetings--index.md patterns/effective-meetings--master.md
multimarkdown --to=mmd --output=patterns/making-and-evolving-agreements--index.md patterns/making-and-evolving-agreements--master.md
multimarkdown --to=mmd --output=patterns/navigation--index.md patterns/navigation--master.md
multimarkdown --to=mmd --output=patterns/organizational-structure--index.md patterns/organizational-structure--master.md
multimarkdown --to=mmd --output=patterns/roles--index.md patterns/roles--master.md
