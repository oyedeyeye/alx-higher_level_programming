#!/usr/bin/python3
"""Module 2: Is_same_class
function that returns True
if the object is exactly an instance of the specified class;
otherwise False"""


def is_same_class(obj, a_class):
    """checks if the obj is an instance of the class

    Args:
        obj (object): an object argument
        a_class (class): a class argument
    Return: True or False
    """

    return type(obj) == a_class
