#!/usr/bin/python3
"""Locked class that prevents dynamic creation of new instance attributes,
except if the new instance attribute is called first_name
"""


class LockedClass():
    """
    prevent dynamic creation of new instance attribute

    >>> a = LockedClass
    >>> a.first_name = 'Noel'
    >>> a.firstname
    'Noel'

    """

    __slots__ = "first_name"
