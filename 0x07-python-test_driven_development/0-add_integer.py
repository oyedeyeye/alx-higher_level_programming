#!/usr/bin/python3

"""Module-0: A method that returns an int sum
Accepts two value, int or float and cast both to int before addition

Args:
        a(int or float): integer or float parameter
        b(int or float): integer or float parameter defaults to 98"""

def add_integer(a, b=98):
    """add_integer function

    Returns a + b as int"""

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
