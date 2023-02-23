#!/usr/bin/python3
"""Module 6: Base geometry
with public instance methods"""


class BaseGeometry:
    """Class with public instance method

    Methods:
        area: computes area of the geometry
        integer_validator: validates integer values
    """

    def __init__(self, size=0, width=0):
        pass

    def integer_validator(self, name, value):
        """integer validator

        Args:
            name (str): always a string
            value (int): greater than 0
        """
        self.name = name
        self.value = value

        if type(self.value) is not int:
            raise TypeError("{:s} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(self.name))

    def area(self):
        raise Exception("area() is not implemented")
