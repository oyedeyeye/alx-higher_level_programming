#!/usr/bin/python3
"""
MOdule 3-square
Define class square with private instance attribute size,
validate size and define a public instance method for computing
the area of the square
"""


class Square:
    """
    class square definition
    Args:
        size (int): length of the side of a square
    """

    def __init__(self, size=0):
        """
        Initializes the square instance

        Attributes:
        __size (int): length of the side of a square,
            defaults to 0 if none
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def area(self):
        """
        Public instance that computes the area of the square

        Returns:
            area
        """
        return (self.__size)**2
