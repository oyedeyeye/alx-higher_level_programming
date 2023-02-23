#!/usr/bin/python3
"""
Module 101: add_attribute
Adds a new attribute to an object if it’s possible:"""


def add_attribute(obj, attribute, value):
    """adds a new attribute to an object if it’s possible:"""
    if('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribut")
