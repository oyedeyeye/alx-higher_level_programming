#!/usr/bin/python3
"""
Defines MagicCLass that does exactly as the byteCode provided
"""


import math


class MagicClass:
    """ Defines a circle"""

    def __init__(self, radius=0):
        """
        Initializes a magicClass

        Args:
            radius (float or int): The radius of the new MagicCLass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Define the area of the magicClass"""
        return (math.pi * self.__radius ** 2)

    def circumference(self):
        """Define the circumference of the MagicCLass"""
        return (2 * math.pi * self.__radius )