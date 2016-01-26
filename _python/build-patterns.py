#!/usr/bin/env python

import argparse
import os

from s3_patterns import s3_patterns


def make_file(folder, filename_root, title_root):
        with file(os.path.join(folder, make_pathname(filename_root)+ '.md'), 'w+') as fp:
            fp.write('# '+make_title(title_root)+"\n\n...\n")


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


def write_link(fp, link_title, link_path):
    fp.write("\t* [%s](%s)\n" % (link_title, link_path))


def build_toc_files(patterns):
    """(Re-)build all includes with tables of contents."""
    create_directory('patterns')
    
    # create /_toc_include.md to be included in the main index
    write_toc_include(patterns, '_index--toc.md', '/patterns/') # root patterns index
    write_toc_include(patterns, os.path.join('patterns', '_full_index.md')) # patterns index
    write_toc_include(sorted(s3_patterns.keys()), os.path.join('patterns', '_index_groups_toc.md')) # groups TOC

    # build a TOC for each group
    for group in s3_patterns.keys():
        write_toc_include(sorted(s3_patterns[group]), os.path.join('patterns', '_%s--toc.md' % group)) # groups TOC


def write_toc_include(items, filename, target_prefix=''):
    """Create a table of contents from items and write to filename."""
    with file(filename, 'w+') as fp:
        for item in items:
            write_link(fp, make_title(item), target_prefix+make_pathname(item)+'.md')


def build_skeleton_files(patterns, groups):
    """Build skeleton content files for groups and patterns."""
    
    # create patterns files
    for pattern in patterns:
        make_file('patterns', pattern, pattern)

    # create group content files
    for group in groups:
        make_file('patterns', '_%s--content.md' % group, group)


if __name__ == "__main__":

    # setup argparse
    parser = argparse.ArgumentParser(description='build files for s3 patterns website and handbooks')
    parser.add_argument('--toc', action='store_true',
                        help='(re-)build all includes with tables of contents.')
    parser.add_argument('--skeleton', action='store_true',
                        help='build skeleton content files for groups and patterns.')
    args = parser.parse_args()

    # init
    patterns = get_all_patterns()

    if args.toc:
        build_toc_files(patterns)

    if args.skeleton:
        build_skeleton_files(patterns, s3_patterns.keys())

