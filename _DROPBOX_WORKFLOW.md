# Workflow For Editing In Dropbox

## Format 

The files are in Markdown format, see the [Markdown Primer](http://www.engadget.com/2010/12/29/markdown-primer/) and the official [Markdown Syntax Guide](http://daringfireball.net/projects/markdown/syntax) for details. 

**Note:** There is many different flavours of Markdown, the one we use is plain markdown as described in the guide above, with the addition of "front matter" at the top of the file, enclosed in `---`. For the moment, it just contains the title of the page.

Example: 

    ---
    title: Align Flow
    ---
    
    Some text.


### Headlines

Since the title is headline level 1, all other headlines in a file must be level 2 or more. 


### Changing the Title of a Pattern

Changing the title of a patterns or section in the title of a file is not enough, we need also to change the title in the patterns list (which is not included in the export), and then rebuild all tables of content and group index files.


## Working in Dropbox

Dropbox does not contain all of the project's files, only actual content files and images. This makes it easier to track changes and avoid changing the wrong files. 

At the moment, we have:

* one file for each pattern
* one file for each pattern group (suffixed with `--content`), 
* a changelog where we track changes so users can see what's new in their version
* and the introduction, which is rather large.

All exported files have the suffix `--original.md`. When we start editing them, we rename the suffix to `--draft.md`. Once we agree on the content, we rename them to `.md`, so we can easily see which files are ready to publish.

    .
    └── agreements.md (ready for publishing)
    ├── align-flow--draft.md (draft)
    ├── alignment--content--original.md (file is unchanged)
    └── changelog.md


## Critic Markup

To add comments when reviewing files, we can use [Critic Markpup](http://criticmarkup.com/users-guide.php).

    {>> some comment <<}.

