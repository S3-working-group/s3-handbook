#!/usr/bin/env python

import os


def make_pathname(name):
    return name.lower().replace(" ",'-')


def make_title(name):
    return name.title().replace('s3','S3')


def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
