#!/usr/bin/env python

import argparse
import os

from s3_patterns import s3_patterns


def make_pathname(name):
    return name.lower().replace(" ",'-')


def make_title(name):
    return name.title().replace('s3','S3')


def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def get_all_patterns():
    """Return a sorted list of all patterns."""
    all_patterns = []
    for group in s3_patterns.keys():
        for pattern in s3_patterns[group]:
            all_patterns.append(pattern)
    return sorted(all_patterns)


def build_toc_files(args, patterns):
    """(Re-)build all includes with tables of contents."""
    create_directory('patterns')

    def write_link(fp, link_title, link_path):
        fp.write("\t* [%s](%s)\n" % (link_title, link_path))

    def write_toc_include(items, filename, target_prefix=''):
        """Create a table of contents from items and write to filename."""
        with file(filename, 'w+') as fp:
            for item in items:
                write_link(fp, make_title(item), target_prefix+make_pathname(item)+'.md')

    def write_group_master(folder, group):
            with file(os.path.join(folder, '%s--index.md' % make_pathname(group)), 'w+') as fp:
                fp.write('\n{{%s--content.md}}\n' % group)
                fp.write('\n{{%s--toc.md}}\n' % group)                
    
    # create /_toc_include.md to be included in the main index
    write_toc_include(patterns, 'index--toc.md', '/patterns/') # root patterns index
    write_toc_include(patterns, os.path.join('patterns', 'all_patterns.md')) # patterns index
    write_toc_include(sorted(s3_patterns.keys()), os.path.join('patterns', 'index--groups--toc.md')) # groups TOC

    # build a TOC for each group
    for group in sorted(s3_patterns.keys()):
        write_toc_include(sorted(s3_patterns[group]), os.path.join('patterns', '%s--toc.md' % group)) # groups TOC
        write_group_master('patterns', group)
        if args.verbose:
            # output multimardown command to create build group index files
            print 'multimarkdown --to=mmd --output=patterns/%(group)s--index.md patterns/%(group)s--index--master.md' % {'group': make_pathname(group)}


def build_skeleton_files(args, patterns, groups):
    """Build skeleton content files for groups and patterns."""
    
    def make_file(folder, filename_root, title_root):
            with file(os.path.join(folder, '%s.md' % make_pathname(filename_root)), 'w+') as fp:
                fp.write('# %s\n\n...\n' % make_title(title_root))

    # create patterns files
    for pattern in patterns:
        make_file('patterns', pattern, pattern)

    # create group content files
    for group in groups:
        make_file('patterns', '%s--content.md' % group, group)


if __name__ == "__main__":

    # setup argparse
    parser = argparse.ArgumentParser(description='build files for s3 patterns website and handbooks')
    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('--toc', action='store_true',
                        help='(re-)build all includes with tables of contents.')
    parser.add_argument('--skeleton', action='store_true',
                        help='build skeleton content files for groups and patterns.')
    args = parser.parse_args()

    # init
    patterns = get_all_patterns()

    if args.toc:
        build_toc_files(args, patterns)

    if args.skeleton:
        build_skeleton_files(args, patterns, s3_patterns.keys())

