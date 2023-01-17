#!/usr/bin/python3
"""
module 1-Rectangle
Defines an Rectangle class
"""


class Rectangle:
    """Represents the Rectangle class

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes the rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for width attribute
        Return:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter

        Args:
            value: sets width to value, if it is type int
                    and > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
            return
        elif value < 0:
            raise ValueError("width must be >= 0")
            return

        self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute
        Return:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Args:
            value: sets height to value, if it is type int
                    and > 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
            return
        elif value < 0:
            raise ValueError("height must be >= 0")
            return

        self.__height = value
