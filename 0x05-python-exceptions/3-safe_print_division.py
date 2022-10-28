#!/usr/bin/python3
# function that divides 2 integers and prints the result.
def safe_print_division(a, b):
    try:
        result = a / b
    except:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
