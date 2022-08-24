#!/usr/bin/python3
c = 97
while c <= 122:
    if c != 101 and c != 113:
        print("{}".format(chr(c)), end='')
    c += 1
