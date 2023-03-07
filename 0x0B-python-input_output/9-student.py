#!/usr/bin/python3
"""Module 9: student
Class Student that defines student

methods:
        def __init__(self, first_name, last_name, age)
        def to_json(self)"""


class Student:
    """student attributes

        Public Instance Attributes:
        first_name (str): string type input
        last_name (str): string type input
        age (int): age in years
    """

    def __init__(self, first_name, last_name, age):
        """instantiate the class

            Args:
                first_name (str): string type input
                last_name (str): string type input
                age (int): age in years
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve dictionary representation of Student instance"""
        return self.__dict__
