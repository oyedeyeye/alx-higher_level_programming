#!/usr/bin/python3
"""Script 7: load, add, save
Script that adds all arguments to a Python list, and then save them to a file
Use your function `save_to_json_file` from `5-save_to_json_file.py`
Use your function `load_from_json_file` from `6-load_from_json_file.py`
The list must be saved as a JSON representation in a file named `add_item.json`
If the file doesn’t exist, it should be created
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""Open the add_item.json file in append mode
to create it if it does not exist"""
with open('add_item.json', 'a+', encoding="utf-8") as f:
    f.readline()

f_list = []
if load_from_json_file('add_item.json') is not None:
    f_list += list(load_from_json_file('add_item.json'))

arguments = sys.argv[1:]
for item in arguments:
    f_list.append(item)

save_to_json_file(f_list, 'add_item.json')
