#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for i in range(len(matrix)):
        subMatrix = []
        for j in range(len(matrix[i])):
            subMatrix.append(matrix[i][j] ** 2)
        newMatrix.append(subMatrix)
    return newMatrix
