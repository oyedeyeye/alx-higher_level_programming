#!/usr/bin/python3
c = 0
while c <= 89:
    if c != 89:
        i = c // 10
        j = c % 10
        if i != j and i < j:
            print("{:02d}".format(c), end=', ')
    else:
        print("{}".format(c))
    c += 1
