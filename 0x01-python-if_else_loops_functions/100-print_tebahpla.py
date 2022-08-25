#!/usr/bin/python3
i = 122
while i >= 97:
    j = i
    if j % 2 != 0:
        j -= 32

    print("{}".format(chr(j)), end='')
    i -= 1
