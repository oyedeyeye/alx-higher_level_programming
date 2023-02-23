#!/usr/bin/python3
"""Module 9: Full Rectangle
inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from Base Geometry

    Args:
        width: private atrributes
        height: private attributes
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """computes the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
