#!/usr/bin/python3
def print_last_digit(number):
    if number < 1:
        number *= -1
    ld = number % 10
    print("{}".format(ld), end='')
    return (ld)
