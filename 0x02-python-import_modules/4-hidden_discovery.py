#!/usr/bin/python3
import hidden_4
import sys

if __name__ == "__main__":
    names = dir(hidden_4)

    for i in range(1, len(names)):
        if names[i][0] != '_':
            print("{}".format(names[i]))
