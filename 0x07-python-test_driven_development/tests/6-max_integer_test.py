#!/usr/bin/python3
"""Unittest for max_integer(list)
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class testMaxInteger(unittest.TestCase):
    """ run the test with python3 -m unittest tests.6-max_integer_test"""

    def setUp(self):
        """All our test variables here"""
        self.list1 = [3, 4, 5, 7, 12]  # int type
        self.list2 = [-2, -4, -5, -7, -1]  # negative int types
        self.list3 = [-3.4, 0.5, -5.2, 0.7, -1.2]  # float type
        self.list4 = [10, -10, 10]  # equal number
        self.list5 = [{1, 9}, {2}, {3}]  # list of other types
        self.list6 = [0]  # single element list
        self.str1 = "837629"  # strings
        self.str2 = "mnoadjx"
        self.str3 = ['a', 'b', 'c', 't', 'n', 'z']  # list of letters
        self.str4 = ["abc", "y"]
        # List of list
        self.list7 = [[1, 3], [2, 3], [1, 4], [2, 5]]
        # sequence of other types
        self.others1 = {1, 2, 5, 7}
        self.others2 = {1, 2, 3, 4, 6}
        self.others3 = [1, -2, "abc", {3, 4, 1}]
        # boolean and none types
        self.others4 = [None, True]
        self.others5 = []
        self.others6 = [None]

    def test_module_docstring(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_function_docstring(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)

    def test_number_list(self):
        self.assertEqual(max_integer(self.list1), 12)
        self.assertEqual(max_integer(self.list2), -1)
        self.assertEqual(max_integer(self.list3), 0.7)
        self.assertEqual(max_integer(self.list4), 10)
        self.assertEqual(max_integer(self.list5), {1, 9})
        self.assertEqual(max_integer(self.list6), 0)

    def test_list_of_list(self):
        self.assertEqual(max_integer(self.list7), [2, 5])

    def test_list_of_strings(self):
        self.assertEqual(max_integer(self.str1), "9")
        self.assertEqual(max_integer(self.str2), 'x')
        self.assertEqual(max_integer(self.str3), 'z')
        self.assertEqual(max_integer(self.str4), 'y')

    def test_other_sequence(self):
        with self.assertRaises(TypeError):
            max_integer(self.others1)
        with self.assertRaises(TypeError):
            max_integer(self.others1, self.others2)
        with self.assertRaises(TypeError):
            max_integer(self.others3)
        with self.assertRaises(TypeError):
            max_integer(self.others4)

    def test_None(self):
        self.assertIsNone(max_integer(self.others5), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer(self.others6), None)


if __name__ == '__main__':
    unittest.main()
