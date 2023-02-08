#!/usr/bin/python3
"""
Module 5: Text_indentation
Print two newline characters after `.`, `?` and `:`
"""


def text_indentation(text):
    """Function to print a text with 2 new lines
    After each of these characters: ., ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in ".?:":
        text = text.replace(i, i + "\n\n")
    lines_list = [line.strip(' ') for line in text.split('\n')]
    revised_text = '\n'.join(lines_list)
    print(revised_text)
