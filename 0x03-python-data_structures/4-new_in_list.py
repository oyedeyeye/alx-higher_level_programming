#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    shadowCopy = my_list.copy()
    if idx < 0:
        return shadowCopy
    elif idx > len(shadowCopy) - 1:
        return shadowCopy
    shadowCopy[idx] = element
    return shadowCopy
