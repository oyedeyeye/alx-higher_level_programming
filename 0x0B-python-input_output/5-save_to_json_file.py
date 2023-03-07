#!/usr/bin/python3
"""Module 5: save_to_json_file
Function that writes an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Writes an object to text file, using JSON representation

    Args:
        my_object: a python input type
        filename: file to be written to
    """

    import json

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj, sort_keys=True))
