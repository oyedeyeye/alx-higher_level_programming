#!/usr/bin/python3
"""
module 7-Rectangle
Defines an Rectangle class
"""


class Rectangle:
    """Represents the Rectangle class

    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        number_of_instances: increments on new instance and
                                decrements on deletion(__del__)
        print_symbol: symbol for printing rectangle shape

    Attributes:
        number_of_instances
        print_symbol
        __init__(self)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """Return the printable representation of the Rectangle
        Represents the rectangle with '#'
        """
        if self.__height == 0 or self.__width == 0:
            return ("")

        printable = "\n".join([str(self.print_symbol)
                              * self.__width for i in range(self.__height)])
        return printable

    def __repr__(self):
        """String representation to create new instance"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of the Rectangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
