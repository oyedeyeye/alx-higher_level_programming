#!/usr/bin/python3
def no_c(my_string):
    newString = ''
    for letter in range(len(my_string)):
        if my_string[letter] != 'c' and my_string[letter] != 'C':
            newString += my_string[letter]
    return newString
