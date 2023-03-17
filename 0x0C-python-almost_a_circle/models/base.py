#!/usr/bin/python3
"""Base Class
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""


class Base:
    """The base of all other classes in the package

    Attributes:
        __nb_objects (int): private attributes
        id (int): public instance attribute, default to None

    Methods:
        __init__(self, id=None):
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
