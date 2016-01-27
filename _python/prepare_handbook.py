#!/usr/bin/env python

import argparse
import os

from s3_patterns import s3_patterns, handbook_group_order, all_patterns
from common import make_pathname, make_title, create_directory

def prepare_handbook(args):
    """Prepare all source files so handbook can be compiled through mmd/latex and pandoc/epub."""
    patterns = all_patterns()
    dst_dir = os.path.join('handbook', 'tmp')

    create_directory(dst_dir)
    if set(handbook_group_order) != set(s3_patterns.keys()):
        raise Exception("ERROR: Handbook group order does not reflect actual pattern groups!")

    # copy_all_files_to_tmp(dst_dir, patterns)
	# 2. remove front matter, add titles with correct level to patterns and groups
	# 3. build the master file with transclude files for all patterns and groups
	# 4. transclude and build happens in build-handbook.sh

	
def copy_all_files_to_tmp(dst_dir, patterns):
    """Copy all pattern and group--content files to handbook/tmp."""
    for pattern in patterns:
        shutil.copy('%s.md' % make_pathname(pattern), dst_dir)

    for group in sorted(s3_patterns.keys()):
        shutil.copy('%s.md' % make_pathname(group), dst_dir)        

    shutil.copy('changelog.md', dst_dir)        


if __name__ == "__main__":

    # setup argparse
    parser = argparse.ArgumentParser(description='copy and prepare markdown files for compiling the handbook.')
    parser.add_argument('--verbose', '-v', action='count')

    args = parser.parse_args()
    prepare_handbook(args)
