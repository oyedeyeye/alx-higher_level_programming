#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not []:
        sum = 0
        unique_list = list(set(my_list))
        print(unique_list)
        for i in unique_list:
            sum += i
        return sum
