#!/usr/bin/python3
"""
MOdule 5-square
Define class square with private instance attribute size,
validate size and define a public instance method for computing
the area of the square. Can access and update size
prints to the stdout the square with the character #
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
        size (int): length of the side of a square,
            defaults to 0 if none; do not use __size to call setter
        """
        self.size = size

    @property
    def size(self):
        """
        Getter

        Return:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: sets size to val, if it is type int
                and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def area(self):
        """
        Public instance that computes the area of the square

        Returns:
            area
        """
        return (self.__size)**2

    def my_print(self):
        """
        Public instance method to print in
        stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
