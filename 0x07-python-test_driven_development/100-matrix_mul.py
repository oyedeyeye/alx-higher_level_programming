#!/usr/bin/python3
"""Module Matrix_mul(m_a, m_b)
Function that multiplies e matrices (list of lists)
"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]] or len(m_a) is None:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]] or len(m_b) is None:
        raise ValueError("m_b can't be empty")

    len_inner_a = len(m_a[0])
    for inner_list_a in m_a:
        if not isinstance(inner_list_a, list):
            raise TypeError("m_a must be a list of lists")
        if len(inner_list_a) != len_inner_a:
            raise TypeError("each row of m_a must be of the same size")
            """Nos of cols in matrix A must be == nos of rows in matrix B"""
        if len(inner_list_a) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")
        for elem_a in inner_list_a:
            if not isinstance(elem_a, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    len_inner_b = len(m_b[0])
    for inner_list_b in m_b:
        if not isinstance(inner_list_b, list):
            raise TypeError("m_b must be a list of lists")
        if len(inner_list_b) != len_inner_b:
            raise TypeError("each row of m_b must be of the same size")
        for elem_b in inner_list_b:
            if not isinstance(elem_b, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    new_matrix = []
    for i in range(len(m_a)):  # rows in matrix m_a
        inner_elem = []
        n = 0
        for j in range(len(m_b[0])):  # cols in matrix m_b
            for k in range(len(m_b)):  # rows in matrix m_b
                n += m_a[i][k] * m_b[k][j]
            inner_elem.append(n)
            n = 0
        new_matrix.append(inner_elem)

    return new_matrix
