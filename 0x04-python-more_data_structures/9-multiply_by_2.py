#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDictionary = {}
    for k, v in a_dictionary.items():
        newDictionary[k] = v * 2
    return newDictionary
