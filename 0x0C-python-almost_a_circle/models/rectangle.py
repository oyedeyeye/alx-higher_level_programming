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
        id: identity of the rectangle class
        *args: pass non-keyworded vaariable length argument list to function

    Methods:
        def __init__(self, width, height, x=0, y=0, id=None):
        def area(self):
        def display(self):
        def update(self, *args):
        def __str__(self):
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

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
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value=0):
        """Setter for x

        Args:
            value: the value for x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value=0):
        """Setter for y

        Args:
            value: the value for y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """computes area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints Rectangle instance with character `#`"""

        if self.__y > 0:
            print("{}".format('\n' * self.__y), end='')
        if self.__x > 0:
            print(
                "\n".join([((' ' * self.__x) + ('#' * self.__width))
                          for i in range(self.__height)]))
        else:
            print(
                "\n".join(['#' * self.__width for i in range(self.__height)]))

    def update(self, *args):
        """Public method that assigns argument to each attributes"""
        attrs = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            if i >= len(attrs):
                break
            setattr(self, attrs[i], arg)

    def __str__(self):
        """Return the printable representation of the Rectangle class"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)
