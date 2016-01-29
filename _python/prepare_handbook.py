#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import shutil

from s3_patterns import s3_patterns, handbook_group_order, all_patterns
from common import make_pathname, make_title, create_directory
from convert_jekyll_files import copy_and_fix_headlines


def prepare_handbook(args):
    """Prepare all source files so handbook can be compiled through mmd/latex and pandoc/epub."""
    patterns = all_patterns()
    dst_dir = os.path.join('handbook', 'tmp')

    create_directory(dst_dir)
    if set(handbook_group_order) != set(s3_patterns.keys()):
        raise Exception(
            "ERROR: Handbook group order does not reflect actual pattern groups!")

    convert_and_copy_all_files_to_tmp(dst_dir, patterns)
    create_master_file_with_all_patterns(dst_dir)


def convert_and_copy_all_files_to_tmp(dst_dir, patterns):
    """
    Copy all pattern and group--content files to handbook/tmp, 
    convert front matter title to headline and adapt all headline levels as required.
    """
    for pattern in patterns:
        copy_and_fix_headlines(dst_dir, '%s.md' % make_pathname(pattern), 3)

    for group in sorted(s3_patterns.keys()):
        copy_and_fix_headlines(
            dst_dir, '%s--content.md' % make_pathname(group), 2)

    copy_and_fix_headlines(dst_dir, 'introduction.md', 1)
    copy_and_fix_headlines(dst_dir, 'changelog.md', 2)


def create_master_file_with_all_patterns(dst_dir):
    """Create tmp/patterns--master.md with transcludes for all groups and their patterns."""
    with file(os.path.join(dst_dir, 'patterns--master.md'), 'w+') as fp:
        for group in handbook_group_order:
            fp.write('\n\n{{%s--content.md}}\n' % make_pathname(group))
            for pattern in sorted(s3_patterns[group]):
                fp.write('\n{{%s.md}}\n' % make_pathname(pattern))


if __name__ == "__main__":

    # setup argparse
    parser = argparse.ArgumentParser(
        description='copy and prepare markdown files for compiling the handbook.')
    parser.add_argument('--verbose', '-v', action='count')

    args = parser.parse_args()
    prepare_handbook(args)
