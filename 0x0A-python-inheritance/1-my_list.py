#!/usr/bin/python3
"""Module 1 - MyList
class that inherits from list"""


class MyList(list):
    """inherits from the list class with a sort method

    methods:
    print_sorted(self)
    """

    def print_sorted(self):
        """returns sorted list in ascending order"""
        print(sorted(self))
