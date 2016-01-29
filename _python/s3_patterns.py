#!/usr/bin/env python

handbook_group_order = [

    "making and evolving agreements",
    "navigation",
    "effective meetings",
    "coordinating work",
    "building organizations",
    "roles",
    "organizational structure",
    "bringing in S3 patterns",
    "alignment",
]

s3_patterns = {
    "alignment": [
        "adopt S3 principles",
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
        "domains",
        "open systems",
        "organizing in circles",
        "subset drivers",
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
        "evaluating decisions",
        "evaluation criteria",
        "intended outcome",
        "objections",
        "proposal forming",
        "qualifying drivers",
        "resolve objections",
        "strategy",
        "those affected decide",
    ],
    "navigation": [
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
    "roles": [
        "development plan",
        "effectiveness review",
        "role descriptions",
        "role selection",
        "support roles",
    ],
}


def all_patterns():
    """Return a sorted list of all patterns."""
    all_patterns = []
    for group in s3_patterns.keys():
        for pattern in s3_patterns[group]:
            all_patterns.append(pattern)
    return sorted(all_patterns)
