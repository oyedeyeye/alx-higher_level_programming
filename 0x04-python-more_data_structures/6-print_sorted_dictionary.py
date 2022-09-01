#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list = list(a_dictionary.keys())
    for k in sorted(key_list):
        print("{}: {}".format(k, a_dictionary[k]))
