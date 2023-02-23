#!/usr/bin/python3
"""Module 6: Base geometry
with public instance method"""


class BaseGeometry:
    """Class with public instance method 

    Methods:
        area
    """

    def __init__(self, size=0, width=0):
        self.size = size
        self.width = width

    def area(self):
        raise Exception("area() is not implemented")
