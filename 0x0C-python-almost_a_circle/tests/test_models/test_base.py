#!/usr/bin/python3
"""Testing Suite for the base class"""

import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """testing models/base.py"""

    def setUp(self):
        """initialize variables"""
        Base._Base__nb_objects = 0  # reset the number of objects

    def tearDown(self):
        """reset variable"""

    def test_baseClasswithArgs(self):
        """test no args instances of Base class"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(50)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 50)
        self.assertEqual(b5.id, b3.id + 1)

    def test_None_Arg(self):
        """test that Base is a class"""
        b1 = Base(None)
        b2 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)


if __name__ == '__main__':
    unittest.main()
