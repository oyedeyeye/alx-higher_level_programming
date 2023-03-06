#!/usr/bin/python3
"""Module 4: from_json_string
Function that returns an object (Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """returns an object from a JSON representation

    Args:
        my_str: JSON string"""

    import json

    return json.loads(my_str)
