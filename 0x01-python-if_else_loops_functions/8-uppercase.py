#!/usr/bin/python3
def uppercase(str):
    i = 0
    _newStr = ''
    while i < len(str):
        j = ord(str[i])
        if j >= 97 and j <= 122:
            _newStr += chr(j - 32)
        else:
            _newStr += str[i]
        i += 1
    print("{}".format(_newStr))
