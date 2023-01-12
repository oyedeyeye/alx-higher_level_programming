#!/usr/bin/python3
"""
Module 1-square
Define class Square with private attribute size
"""


class Square:
    """ class square definition
    Args:
        size: length of the side of a square
    """
    def __init__(self, size):
        """
        Initializes square instance

        Attributes:
            size: length of the side of a square
        """
        self.__size = size
