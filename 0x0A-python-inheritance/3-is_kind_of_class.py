#!/usr/bin/python3
"""Module 3: Is_kind_of_class
function that returns True
if the object is an instance of a class that inherited from,
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """checks if the obj is an instance of the class

    Args:
        obj (object): an object argument
        a_class (class): a class argument
    Return: True or False
    """

    return isinstance(obj, a_class)
