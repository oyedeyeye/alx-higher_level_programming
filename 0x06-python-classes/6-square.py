#!/usr/bin/python3
"""
MOdule 6-square
Define class square with private instance attribute size and position
validate both by defining @property of each,
define a public instance method for computing
the area of the square. Use Getters and Setters to
access and update size and position
prints to the stdout the square with the character #
"""


class Square:
    """
    class square definition
    Args:
        size (int): length of the side of a square
        position (int): tuple of 2 positive integers
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square instance

        Attributes:
        size (int): length of the side of a square,
            defaults to 0 if none; do not use __size to call setter
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter

        Return:
            position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter

        Args:
            value (tuple): sets position to value
            if value is tuple of 2 positive integers
        """
        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            print("")
        else:
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
