#!/usr/bin/python3
"""Module 6: peak
function that finds a peak in a list of unsorted integers.

Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity (hint: you dont
need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your algorithm:
O(log(n)), O(n), O(nlog(n)) or O(n2)
Note: there may be more than one peak in the list
"""


def find_peak(list_of_integers):
    """returns peak in a list of unsorted integers

    Args:
        list_of_integers (list): an unsorted list
    """
    if list_of_integers == []:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    # checking first and last element of the list
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]

    # using binary search to find peak
    left, right = 1, len(list_of_integers) - 2
    while left <= right:
        mid = (left + right) // 2
        if list_of_integers[mid - 1] < list_of_integers[
                                        mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1
