#!/usr/bin/python3
"""Module 100: append_after
function that inserts a line of text to a file,
After each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends line of text into a file

    Args:
        filename: a file
        search_string (str): a string parameter
        new_string (str): a string parameter
    """
    with open(filename, "r", encoding="utf-8") as f:
        str_text = f.readlines()
        f_list = []
        for row in str_text:
            if row.find(search_string) != -1:
                f_list.append(row)
                f_list.append(new_string)
            else:
                f_list.append(row)
    with open(filename, "w", encoding="utf-8") as g:
        g.write("".join(f_list))
