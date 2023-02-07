#!/usr/bin/python3
"""
Module: 3 say first name and last name
Takes two string arguments and prints out a string with the names
Args:
    first_name: a string
    last_name: a string, defaults to ""
"""


def say_my_name(first_name, last_name=""):
    """Function that prints my name"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
