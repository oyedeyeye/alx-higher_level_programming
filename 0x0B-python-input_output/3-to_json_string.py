#!/usr/bin/python3
import json
"""Module 3: to_json_string
function that returns the JSON representation of an object (string):
"""


def to_json_string(my_obj):
    """Returns the JSON representation of the object
    
    Args:
        my_obj: an object intput type"""
    return json.dumps(my_obj, sort_keys=True)
