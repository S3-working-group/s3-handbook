# S3 Patterns Repository

This is the source files of the canonical Sociocracy 3.0 patterns repository.


## Driver

As more people and organizations started picking up 3, the need for a handbook with short descriptions of all patterns became obvious. Also, the patterns repository answers the common question what is James and Bernhard consider to be the body of S3 patterns, what S3 is (and is not).


## Download and Following Updates

The easiest way to download the handbooks is either through the [S3 website](http://sociocracy30.org) or through Github. 

You can follow changes by looking at this repository's history on Github, or taking a look at the changelog in the handbook or in **/patterns/changelog.md**


## Formats and Files

Content is stored as [MarkDown](http://daringfireball.net/projects/markdown) files with the extension `.md`. Markdown can be edited with any text editor, rendered to html, pdf, and latex with various apps on any relevant platform, and converted into countless[^not literally] other formats, e.g. epub, using [pandoc](https://github.com/jgm/pandoc).


### Publishing

The **handbook** is compiled from many individual Markdown files using MultiMarkdown and file transclusion. The resulting Markdown document is rendered to **pdf** using the [MultiMarkdown](http://fletcherpenney.net/multimarkdown/) commandline tool and LaTex, and to **ebub** with pandoc. 

The **web version** is generated thorugh Jekyll, a static site generator which can also be used to publish to Gihub pages.

{>>TODO: exclude scripts in config.yaml <<}

## Handbook Headline Structure

Working with several different tools at the same time has some drawbacks, one of which is the headline levels, which must be correct for the pdf and epub version of the handbook.

This means that pattern descriptions start at headline level 2 (`###`), and pattern groups start at headline level 2 (`##`). 

Another limitation is the location of the image files, which must be in the same relative path for both the web version and the handbook version, this is why all content files linking to images need to be in the same folder.

In order to keep the include files, stylesheets etc. of the handbook out of the `/patterns` directory, a symlink with the relative path to the images folder is kept in the handbook build folder, this works well on OS-X and Linux, but may not work on Windows.


### Content files

**Pattern descriptions** are created in the folder `/patterns/` as individual Markdown files. 

{>>TODO: update file generator for flat structure <<}

Each **pattern group** has a brief description in a file prefixed with an underscore, and suffixed with `--content`, e.g. `/patterns/_navigation_content.md`. 

A **changelog** is maintained in `/patterns/_changelog.md` and integrated both in the appendix of the handbook and as a subpage of the website.

A content for the **root level index file** is kept in `/_index--content.md` and serves as the Github intro page, content for the **patterns index page** can be found in `/patterns/_index--content.md`

**Images** are stored in */patterns/img/* and must be included using relative paths.

## Creating the HTML Version

There's a Github pages **intro page** at `/index.md`, compiled from `/_index--content.md`, and a full table of contents from `/_index--toc.md`

{>>TODO: build skeleton with includes, create files <<}
{>>TODO: include changelog in root index <<}

The **patterns index** at `patterns/index.md` draws content from `/patterns/_index--content.md`, links to all groups from `/patterns/_index_groups_toc.md` and a complete full alphabetical index of all patterns from `/patterns/_full_index.md`.

{>>TODO: create and build all files described here. <<}
{>>TODO: link index to changelog <<}

Pattern groups indexes (e.g. `/patterns/navigation.md`) include a brief description (e.g. from `/patterns/_navigation--content.md`) and a table of contents (e.g. `/patterns/_navigation--toc.md`)

## Publishing the Handbook

All files relevant to building the handbook are maintained in `/_compile_handbook/`, e.g. styles, master documents. The handbook is compiled form the handbook master file file _handbook-master.md to pdf using the [MultiMarkdown](http://fletcherpenney.net/multimarkdown/) commandline and LaTex, and to epub through pandoc. 

{>>TODO: create handbook master <<}
{>>TODO: create and test pdf buildscript for LaTeX, add styles <<}
{>>TODO: create and test epub buildscript, add styles <<}

The **handbook** is exported to **S3-patterns-handbook.pdf** and **S3-patterns-handbook.epub** in the root folder of the project.

{>>TODO: create document and html indices: toc + text <<}


## Dependencies

{>>TODO: describe dependencies <<}


## To Do

{>>TODO: create template with style to limit image width to 100% <<}
{>>TODO: remove all unnecessary jekyll default stuff <<}
{>>TODO:  update or remove index.html <<}
{>>TODO: include footer with (c) and license, and navigation <<}
{>>TODO: add a second build for popup windows <<}
{>>TODO: move source files to source folder? <<}


## Criteria and Considerations for the Technical Implementation

* How can we develop the patterns descriptions and publish them both to the web and to a pdf or epub handbook and avoid duplication or extensive synchronization of content?
* How can we transparently regroup patterns and rename pattern groups without affecting URLs of the patterns?
* How can we add images in a transparent way for both HTML and pdf/epub output?
* How can we provide the source files from the patterns descriptions in an open format to promote reuse? 
* How can we integrate the patterns description into the [S3 homepage](http://sociocracy30.org)?
* How can we make it easy to track changes?
* How can we collaborate on the content without requiring all co-authors to use git?
* How can we work on drafts without having to publish half-finished descriptions?


## Drafts and Collaboration

We publish the skeleton site with empty pages for each pattern and pattern group. A copy of the skeleton site is placed in dropbox, al files are suffixed with "--draft", we copy all existing texts into that skeleton. As soon as we finish a releasable version of a pattern, we remove the draft suffix, merge the changes into the repository and re-publish. 

Updates to existing patterns are created in the dropbox copy and then merged back.


## License 

This work by Bernhard Bockelbrink and James Priest is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/).
