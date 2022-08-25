#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    
    j = len(argv)

    if j == 1:
        print("{} arguments.".format(j - 1))
    elif j - 1 == 1:
        j -= 1
        print("{} argument:".format(j))
        print("{}: {}".format(j, str(argv[j])))
    elif j > 1:
        print("{} arguments:".format(j - 1))
        for i in range(1, j):
            print("{}: {}".format(i, str(argv[i])))
