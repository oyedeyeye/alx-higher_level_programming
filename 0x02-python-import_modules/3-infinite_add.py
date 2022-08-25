#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    j = len(argv)
    sum = 0

    for i in range(1, j):
        sum += int(argv[i])

    print("{}".format(sum))
