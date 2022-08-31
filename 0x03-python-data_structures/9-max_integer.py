#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != []:
        max = my_list[0]
        for k in my_list:
            if k > max:
                max = k
        return max
    return None
