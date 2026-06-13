#!/usr/bin/python3
"""Module for dividing all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: list of lists of integers/floats
        div: number to divide by

    Returns:
        New matrix with all elements divided by div
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(msg)
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(msg)
    size = len(matrix[0])
    if not all(len(row) == size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
