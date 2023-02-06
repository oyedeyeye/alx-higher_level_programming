#!/usr/bin/python3
"""
Module: 2 Divides all the elements of a matrix which contains
A list of list. All elements of the matrix must be divided by
div and rounded to 2 decimal places
"""


def matrix_divided(matrix, div):
    """Matrix function"""

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    same_size = len(matrix[0])
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)

    for i in range(len(matrix)):
        if len(matrix[i]) != same_size:
            raise TypeError("Each row of the matrix must have the same size")

        new_list = []
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(msg)
            new_list.append(matrix[i][j] / div)

        new_matrix.append(new_list)
    return new_matrix
