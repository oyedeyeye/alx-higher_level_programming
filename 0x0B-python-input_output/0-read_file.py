#!/usr/bin/python3
"""Module 0: Read file
Function that reads a text file (UTF-8) and prints it to stdout
"""


def read_file(filename=""):
    """Reads the file passed as argument and prints to stdout

    Args:
        filename: file to be read
        """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            print("{}".format(line), end="")
