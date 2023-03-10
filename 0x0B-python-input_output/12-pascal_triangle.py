#!/usr/bin/python3
"""Module 12: pascal_triangle
returns a list of lists of integers representing the Pascal triangle of n
"""


def pascal_triangle(n):
    """returns list of integer representing pascal triangle"""
    if n <= 0:
        return []
    res_arr = [[1]]

    for i in range(n - 1):
        temp = [0] + res_arr[-1] + [0]
        row = []

        for j in range(len(res_arr[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res_arr.append(row)
    return res_arr
