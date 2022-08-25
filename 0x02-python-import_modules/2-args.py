#!/usr/bin/python3
from sys import argv

j = len(argv) - 1

if j == 1:
    print("{} argument:".format(j))
    print("{}: {}".format(j, str(argv[j])))
elif j > 1:
    print("{} arguments:".format(j))
    for i in range(1, j + 1):
        print("{}: {}".format(i, str(argv[i])))
