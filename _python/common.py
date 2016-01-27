#!/usr/bin/env python

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