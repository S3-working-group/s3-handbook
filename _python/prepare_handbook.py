#!/usr/bin/env python

import argparse
import os

from s3_patterns import s3_patterns
from common import make_pathname, make_title, create_directory, get_all_patterns


def prepare_handbook(args):
	"""Prepare all source files so handbook can be compiled through mmd/latex and pandoc/epub."""
    patterns = get_all_patterns()

	# 1. copy all pattern and group--content files to handbook/tmp
	# 2. remove front matter, add titles with correct level to patterns and groups
	# 3. build the master file with transclude files for all patterns and groups
	# 4. transclude and build happens in build-handbook.sh
	

if __name__ == "__main__":

    # setup argparse
    parser = argparse.ArgumentParser(description='copy and prepare markdown files for compiling the handbook.')
    parser.add_argument('--verbose', '-v', action='count')

    args = parser.parse_args()
	prepare_handbook(args)
