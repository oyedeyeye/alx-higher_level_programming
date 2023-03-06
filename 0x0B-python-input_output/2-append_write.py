#!/usr/bin/python3'
"""Module 2: Append_write
function that appends a string at the end of a text file (UTF8) and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file

    Args:
        filename: file to be modified
        text: string to be added"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
