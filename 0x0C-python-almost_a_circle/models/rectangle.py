#!/usr/bin/python3
"""Class Rectangle that inherits from Base
Private instance attributes, each with its own public getter and setter:

Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - that use logic of the __init__ of Base class
Assign each argument width, height, x and y to the right attribute
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base

    Private Instance Attributes:
        __width : width of the rectangle
        __height : height of the rectangle
        __x: positional argument, defaults to 0
        __y: positional argument, defaults to 0
        id: id of the class passed as argument to super()
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate the class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width

        Args:
            value: the value for width
        """
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height

        Args:
            value: the value for height
        """
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x

        Args:
            value: the value for x
        """
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y

        Args:
            value: the value for y
        """
        self.__y = value
