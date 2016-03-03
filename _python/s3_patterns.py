#!/usr/bin/env python


# Groups:



handbook_group_order = [

    "making and evolving agreements",
    "governance",
    "effective meetings",
    "coordinating work",
    "building organizations",
    "people and roles",
    "organizational structure",
    "bringing in S3 patterns",
    "alignment",
]

s3_patterns = {
    "alignment": [
        "adopt the seven principles",
        "agree on values",
        "bylaws",
        "contracting and accountability",
        "linking",
        "transparent salary",
    ],
    "bringing in S3 patterns": [
        "adapt patterns to context",
        "be the change",
        "continuous improvement of work process",
        "open S3 adoption",
        "pull-system for organizational change",
    ],
    "building organizations": [
        "align flow",
        "open systems",
        "organize in nested domains",
    ],
    "coordinating work": [
        "coordination meeting",
        "coordinator role",
        "daily standup",
        "planning and review meetings",
        "prioritized backlog",
        "pull-system for work",
        "retrospective",
        "visualize work",
    ],
    "effective meetings": [
        "artful participation",
        "logbook keeper",
        "logbook",
        "meeting facilitation",
        "meeting evaluation",
        "rounds",
        "S3 facilitator",
        "secretary",
    ],
    "making and evolving agreements": [
        "agreements",
        "circle",
        "consent decision making",
        "deliverables",
        "driver",
        "evaluate agreements",
        "evaluation criteria",
        "intended outcome",
        "objections",
        "proposal forming",
        "qualifying drivers",
        "resolve objections",
        "strategy",
        "those affected decide",
    ],
    "governance": [
        "navigation backlog",
        "navigation meeting",
        "navigation via tensions",
    ],
    "organizational structure": [
        "backbone organization",
        "coordination circle",
        "delegate circle",
        "double linking",
        "double-linked hierarchy",
        "fractal organization",
        "helping circle",
        "nested circle",
        "peach organization",
        "representative",
        "service circle",
    ],
    "people and roles": [
        "development plan",
        "effectiveness review",
        "role description",
        "role selection",
        "role",
        "support roles",
    ],
}


# TODO: add the seven principles to the handbook

# Renaming process: 
# 1. upate new names in both structures above
# 2. add renames to both structures below
# 3. run the rename tool


groups_to_rename = [

    ('navigation', 'governance'),
    ('roles', 'people and roles'),
]

patterns_to_rename = [

    ("navigation backlog", "governance meeting"),
    ("navigation meeting", "goverance backlog"),
    ('adopt S3 principles', 'adopt the seven principles'),
    ('evaluate decisions', 'evaluate agreements'),
    ('navigating via tensions', 'navigating via tension'),
    ('organizing in circles',  'organize in nested domains'),
    ('role descriptions', 'role description'),
    ('secretary', 'meeting host'),
]


def all_patterns():
    """Return a sorted list of all patterns."""
    all_patterns = []
    for group in s3_patterns.keys():
        for pattern in s3_patterns[group]:
            all_patterns.append(pattern)
    return sorted(all_patterns)
