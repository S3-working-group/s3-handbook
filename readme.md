# S3 Patterns Repository

This is the source files of the canonical Sociocracy 3.0 patterns repository.


## Driver

As more people and organizations started picking up 3, the need for a handbook with short descriptions of all patterns became obvious. Also, the patterns repository answers the common question what is James and Bernhard consider to be the body of S3 patterns, what S3 is (and is not).


## Download and Following Updates

The easiest way to download the handbooks is either through the [S3 website](http://sociocracy30.org) or through Github. 

You can follow changes by looking at this repository's history on Github, or taking a look at the changelog in the handbook or in **/patterns/changelog.md**


## Criteria and Considerations for the Technical Implementation

* ➤ How can we collaborate on the content without requiring all co-authors to use git?
* ➤ How can we work on drafts without having to publish half-finished descriptions?
* How can we develop the patterns descriptions and publish them both to the web and to a pdf or epub handbook and avoid duplication or extensive synchronization of content?
* How can we transparently regroup patterns and rename pattern groups without affecting URLs of the patterns?
* How can we add images in a transparent way for both HTML and pdf/epub output?
* How can we provide the source files from the patterns descriptions in an open format to promote reuse? 
* How can we integrate the patterns description into the [S3 homepage](http://sociocracy30.org)?
* How can we make it easy to track changes?


## Formats and Files

Pattern descriptions are created in the folder */patterns/* as individual MarkDown files. Markdown files can be edited with any text editor, rendered to html, pdf, and latex with various apps on any platform, and converted into countless[^not literally] other formats using [pandoc](https://github.com/jgm/pandoc).

{>>TODO: update file generator for flat structure <<}

Pattern groups each get a file in the same folder, which contains a brief description and links to the individual patterns.

Images are in */patterns/img/* and must be included using a relative paths.

A **changelog** is maintained in */patterns/_changelog.md* and integrated both the appendix of the handbook and as a subpage of the website.

The **handbook** is exported to **S3-patterns-handbook.pdf** and **S3-patterns-handbook.epub** in the root folder of the project.


## Drafts and Collaboration

{>>TODO: describe collaboration <<}


## Publishing

The handbook is compiled form the source file _handbook-master.md to pdf using the [MultiMarkdown](http://fletcherpenney.net/multimarkdown/) commandline and LaTex, and to epub through pandoc. 

Websites are generated thorugh Jekyll, a static site generator which can also be used to publish to Gihub pages.

Scripts for all exports are maintained in the root folder of the repository.

{>>TODO: create and test buildscripts <<}


## Dependencies

{>>TODO: describe dependencies <<}


## License 

This work by Bernhard Bockelbrink and James Priest is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/).
