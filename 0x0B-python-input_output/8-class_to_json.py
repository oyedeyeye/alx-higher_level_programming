#!/usr/bin/python3
"""Module 8: class_to_json
function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """serialize an object (class data structure) in JSON

    Args:
        obj: a class data structure
    """
    import json

    return json.dumps(obj.__dict__, sort_keys=True)
