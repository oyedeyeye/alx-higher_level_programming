#!/usr/bin/python3
# function that executes a function safely.
# Prototype: def safe_function(fct, *args):
# You can assume fct will be always a pointer to a function
# Returns the result of the function,
# Otherwise, returns None if something happens during the function
# and prints in stderr the error precede by Exception:
# You have to use try: / except:
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (ValueError, TypeError, IndexError, ZeroDivisionError) as many_Err:
        result = None
        print("Exception:", many_Err, file=sys.stderr)
        return result
    else:
        return result
