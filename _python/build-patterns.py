#!/usr/bin/env python

import os

s3_patterns = {
    "making and evolving agreements": [
        "resolve objections",
        "driver",
        "evaluating decisions",
        "proposal forming",
        "consent decision making",
        "strategy",
        "objections",
        "agreements",
        "intended outcome",
        "deliverables",
        "evaluation criteria",
        "those affected decide",
        "qualifying drivers",
        "circle",
    ],
    "navigation": [
        "navigation backlog",
        "navigation meeting",
        "navigation via tensions",
    ],
    "effective meetings": [
        "meeting facilitation",
        "S3 facilitator",
        "secretary",
        "meetingevaluation",
        "rounds",
        "logbook",
        "logbook keeper",
        "artful participation",
    ],
    "coordinating work": [
        "retrospective",
        "pull-system for work",
        "visualize work",
        "prioritized backlog",
        "coordinator role",
        "daily standup",
        "coordination meeting",
        "planning and review meetings",
    ],
    "building organizations": [
        "organizing in circles",
        "open systems",
        "subset drivers",
        "align flow",
        "domains",
    ],
    "roles": [
        "role descriptions",
        "role selection",
        "effectiveness review",
        "development plan",
        "support roles",
    ],
    "organizational structure": [
        "double linking",
        "service circle",
        "nested circle",
        "delegate circle",
        "backbone organization",
        "fractal organization",
        "peach organization",
        "double-linked hierarchy",
        "helping circle",
        "role: representative",
        "coordination circle",
    ],
    "alignment": [
        "adopt S3 principles",
        "transparent salary",
        "contracting and accountability",
        "agree on values ",
        "bylaws",
        "linking",
    ],
    "bringing in S3 patterns": [
        "pull-system for organizational change",
        "adapt patterns to context",
        "open S3 adoption",
        "be the change",
        "continuous improvement of work process",
    ]
}


def build():

    # write intex file with links to all patterns an pattern groups
    with file('index.md', 'w+') as fp:
        fp.write('# S3 Patterns\n\n')   
        for group in sorted(s3_patterns.keys()):

            fp.write('* [%s](%s)\n' % (title(group), pathname(group)+'/index.html'))
            for pattern in sorted(s3_patterns[group]):
                fp.write("\t* [%s](%s)\n" % (title(pattern), pathname(group)+'/'+pathname(pattern)+'.md'))


    # process group
    for group in s3_patterns.keys():

        # create dir
        folder = pathname(group)
        if not os.path.exists(folder):
            os.mkdir(folder)

        # create files in dir
        for pattern in sorted(s3_patterns[group]):
            print "   ", title(pattern)
            make_file(folder, pattern, pattern)

        # create index file with links
        with file(os.path.join(folder, 'index.md'), 'w+') as fp:
            fp.write('# '+title(group)+"\n\n")
            for pattern in sorted(s3_patterns[group]):
                fp.write("* [%s](%s)\n" % (title(pattern), pathname(pattern)+'.md'))


def make_file(folder, filename_root, title_root):
        with file(os.path.join(folder, pathname(filename_root)+ '.md'), 'w+') as fp:
            fp.write('# '+title(title_root)+"\n\n")


def pathname(name):
    return name.lower().replace(" ",'-')

def title(name):
    return name.title().replace('s3','S3')


if __name__ == "__main__":
    build()
