#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    new_list = []
    while i < len(my_list):
        if my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])

        i += 1
    return new_list
