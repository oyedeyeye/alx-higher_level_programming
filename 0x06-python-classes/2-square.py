#!/usr/bin/python3
"""
Module 2-square
Define class Square with private instance attribute size
and validates size
"""


class Square:
    """ class square definition
    Args:
        size (int): length of the side of a square
    """

    def __init__(self, size=0):
        """
        Initializes square instance

        Attributes:
            __size (int): length of the side of a square,
                defaults to 0 if none
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
