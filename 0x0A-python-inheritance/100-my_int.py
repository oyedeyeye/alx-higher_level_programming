#!/usr/bin/python3
""""Module: 100 - myInt
class that inherits from the int type
MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """myInt class inherits from int"""
    def __init__(self, num):
        """initialize the class"""
        self.num = num

    def __eq__(self, other):
        """alter behaviour of equal to
        Args:
            other (int): an int argument
        Return True if both are not equal"""
        return self.num != other

    def __ne__(self, other):
        """Returns True if both are equal"""
        return self.num == other
