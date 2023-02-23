#!/usr/bin/python3
"""Module 10: Square subclass
inherits from Rectangle that inherits from BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle

    Methods:
        __init__(self, size)
    """

    def __init__(self, size):
        """initializes size

        Args:
            size (int): private attribute"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    # def area(self):
    #     """computes area of the square"""
    #     return size ** 2
