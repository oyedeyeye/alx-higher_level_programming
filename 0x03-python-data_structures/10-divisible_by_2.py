#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list != []:
        newList = []
        for k in my_list:
            if k % 2 == 0:
                newList.append(True)
            else:
                newList.append(False)
        return newList
