#!/usr/bin/python3
"""Module 6: load_from_json_file
function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """Create object from JSON file

    Args:
        filename: file containing json object"""

    import json

    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            return json.loads(line)
