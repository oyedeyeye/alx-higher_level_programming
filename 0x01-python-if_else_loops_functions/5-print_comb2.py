#!/usr/bin/python3
c = 0
while c <= 99:
    if c != 99:
        print("{:02d}".format(c), end=', ')
    else:
        print("{}".format(c))
    c += 1
