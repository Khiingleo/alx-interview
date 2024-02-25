#!/usr/bin/python3
"""
given an n x n 2D matrix, rotate it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    edits the matrix in-place
    """
    matrix_copy = [[cp for cp in m] for m in matrix]

    i = 0
    for rows in matrix_copy[::-1]:
        j = 0
        for cols in rows:
            matrix[j][i] = cols
            j += 1
        i += 1
