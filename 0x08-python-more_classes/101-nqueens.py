#!/usr/bin/python3
"""
This module contains an algorithm that resolves the
N-Queen puzzle using backtracking
"""


def isSafe(m_queen, nqueen):
    """
    Determines if queens can kill each other

    Args:
        m_queen: array containing the queen's positions
        nqueen: queen number

    Return:
        True: when queens can not kill each other
        False: when queens can kill each other
    """

    for i in range(nqueen):
        if m_queen[i] == m_queen[nqueen]:
            return False

        if abs(m_queen[i] - m_queen[nqueen]) == abs(i - nqueen):
            return False

        return True


def print_result(m_queen, nqueen):
    """
    Prints list with the Queen's positions

    Args:
        m_queen: array containing the queen's positions
        nqueen: queen number
        """

    result = []

    for j in range(nqueen):
        result.append([i, m_queen[i]])

    print(result)


def Queen(m_queen, nqueen):
    """
    Recursive function that executes Backtracking algorithm

    Args:
        m_queen: array containing the queen's positions
        nqueen: queen number
    """
    if nqueen is len(m_queen):
        print_result(m_queen, nqueen)
        return

    m_queen[nqueen] -= 1

    while ((m_queen[nqueen] < len(m_queen) - 1)):
        m_queen[nqueen] += 1

        if isSafe(m_queen, nqueen) is True:

            if nqueen is not len(m_queen):
                Queen(m_queen, nqueen + 1)


def solvedNQueen(size):
    """
    Invokes the Backtracking Algorithms

    Args:
        size: size of the chess board
    """
    m_queen = [-1 for i in range(size)]
    Queen(m_queen, 0)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solvedNQueen(size)
