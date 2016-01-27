#!/usr/bin/env python

import argparse
import os

from s3_patterns import s3_patterns
from common import make_pathname, make_title, create_directory, get_all_patterns


def front_matter(fp, title=''):
    fp.write('---\n')
    if title:
        fp.write('title: %s\n' % title)
    fp.write('---\n\n')


def build_toc_files(args, patterns, root='content-tmp'):
    """(Re-)build all includes with tables of contents."""
    create_directory(root)

    def write_link(fp, link_title, link_path):
        fp.write("* [%s](%s)\n" % (link_title, link_path))

    def write_toc_include(items, filename, target_prefix=''):
        """Create a table of contents from items and write to filename."""
        with file(filename, 'w+') as fp:
            for item in items:
                write_link(fp, make_title(item), target_prefix+make_pathname(item)+'.html')

    def write_group_master(folder, group):
        gpath = make_pathname(group)
        with file(os.path.join(folder, '%s--master.md' % gpath), 'w+') as fp:
            front_matter(fp, make_title(group))
            fp.write('\n{{%s--content.md}}\n' % gpath)
            fp.write('\n{{%s--toc.md}}\n' % gpath)                
    
    write_toc_include(patterns, os.path.join(root, 'all-patterns.md')) # patterns index
    write_toc_include(sorted(s3_patterns.keys()), os.path.join(root, 'index--groups--toc.md')) # groups TOC

    # build a TOC for each group
    for group in sorted(s3_patterns.keys()):
        write_toc_include(sorted(s3_patterns[group]), os.path.join(root, '%s--toc.md' % make_pathname(group)))
        write_group_master(root, group)


def build_skeleton_files(args, patterns, groups, root='content-tmp'):
    """Build skeleton content files for groups and patterns."""
    
    create_directory(root)

    def make_file(filename_root, title_root):
        with file(os.path.join(root, '%s.md' % make_pathname(filename_root)), 'w+') as fp:
            front_matter(fp, make_title(title_root))
            fp.write('\n\n...\n')

    # create patterns files
    for pattern in patterns:
        make_file(pattern, pattern)

    # create group content files
    for group in groups:
        make_file('%s--content' % group, group)


def generate_index_files(root='content'):
    """mmd commands to compile index files from masters."""

    print "# patterns index"
    print 'multimarkdown --to=mmd --output=index.md index--master.md\n'

    print "# group indexes"
    for group in sorted(s3_patterns.keys()):
        # output multimarkdown command to create build group index files
        print 'multimarkdown --to=mmd --output=%(group)s.md %(group)s--master.md' % {'group': make_pathname(group)}        


def list_excluded_files(args, groups):

    def _print(name, suffix):
        print '\t"%s--%s.md",' % (name, suffix)

    for group in sorted(groups):
        group = make_pathname(group)
        for suffix in ['content', 'toc', 'master']:
            _print(group, suffix)


if __name__ == "__main__":

    # setup argparse
    parser = argparse.ArgumentParser(description='build files for s3 patterns website and handbooks')
    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('--toc', action='store_true',
                        help='(re-)build all includes with tables of contents.')
    parser.add_argument('--skeleton', action='store_true',
                        help='build skeleton content files for groups and patterns.')
    parser.add_argument('--excluded', action='store_true',
                        help='Create exclude list for _config.yaml.')
    parser.add_argument('--index', action='store_true',
                        help='Output commands for generate-index-files.')

    args = parser.parse_args()

    # init
    patterns = get_all_patterns()
    root = 'content'

    if args.toc:
        build_toc_files(args, patterns)

    if args.skeleton:
        build_skeleton_files(args, patterns, s3_patterns.keys())

    if args.excluded:
        list_excluded_files(args, s3_patterns.keys())

    if args.index:
        generate_index_files()


