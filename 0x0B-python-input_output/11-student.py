#!/usr/bin/python3
"""Module 11: student
Class Student that defines student

methods:
        def __init__(self, first_name, last_name, age)
        def to_json(self)
        def reload_from_json(self, json):
"""


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

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of Student instance"""
        if attrs is not None:
            dic = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    dic[attr] = self.__dict__[attr]
            return dic
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json: json representation of object
        """
        for key, value in json.items():
            setattr(self, key, value)
