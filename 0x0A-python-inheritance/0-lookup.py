#!/usr/bin/python3
"""Module 0 - Lookup
function that returns list of available attributes and methods of an object
"""


def lookup(obj):
    """Returns list of attributes and methods of object"""
    return dir(obj)
