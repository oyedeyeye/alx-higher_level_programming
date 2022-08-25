#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    j = len(str)
    _str = ''

    while i < j:
        if i != n:
            _str += str[i]
        i += 1

    return _str
