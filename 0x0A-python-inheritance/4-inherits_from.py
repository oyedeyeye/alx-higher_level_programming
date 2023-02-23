#!/usr/bin/python3
"""Module 4: inherits_from
function that returns True
if the object is an instance of a class that inherited (directly
or indirectly) from, the specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """checks if the obj is an instance of the specified class

    Args:
        obj (object): an object argument
        a_class (class): a class argument
    Return: True or False
    """

    return type(obj) is not a_class and issubclass(type(obj), a_class)
