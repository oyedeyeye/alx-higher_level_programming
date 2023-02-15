#!/usr/bin/python3
"""Module 101: Lazy matrix multiplication
Multiplies 2 matrices using the NumPy module
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices using the numpy module"""
    # return np.dot(m_a, m_b)
    return np.matmul(m_a, m_b)
