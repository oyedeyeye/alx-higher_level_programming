#!/usr/bin/python3
"""Module 1: Write to a file
function that writes string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """write text to file and returns the number of characters written

    Args:
        filename: file to be modified
        text: string to be written to the file
        """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
