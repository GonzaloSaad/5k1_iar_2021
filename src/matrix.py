import itertools
from typing import Tuple

import numpy as np


def from_str(matrix_str, input_type=int, column_separator=" ", row_separator="\n") -> np.ndarray:
    """
    Transforms a str representation of a matrix in a numpy array

    example:

        2 2 3 3 1 8
        3 1 4 8 7 4
        9 7 5 5 5 6
        1 2 3 1 3 2
        6 6 7 6 3 3
        7 7 8 6 9 6

    Args:
        matrix_str: string representation of a matrix
        input_type: type to parse the input with
        column_separator: type to parse the input with
        row_separator: type to parse the input with

    Returns:
        list[list]: matrix in str as a numpy array

    """
    matrix = [[input_type(n) for n in line.split(column_separator)] for line in matrix_str.split(row_separator) if line]

    return np.array(matrix)


def get_elements(matrix) -> np.ndarray:
    """
    Gets all the elements in a matrix

    Args:
        matrix: numpy matrix

    Returns:

    """
    elements = list(itertools.chain.from_iterable(matrix))
    return np.array(elements)


def histogram(matrix, grey_scale) -> Tuple[np.ndarray, np.ndarray]:
    """
    Creates a frequency histogram and its normalized counterpart
    Args:
        matrix: matrix to perform the histogram
        grey_scale: grey scale on which to create the histogram

    Returns:
        np.ndarray, np.ndarray

    """
    elements = get_elements(matrix)

    hist = np.zeros(grey_scale + 1)
    for i in range(0, grey_scale + 1):
        frequency = sum(sum(matrix == i))
        hist[i] = frequency

    hist_norm = hist / len(elements)

    return hist, hist_norm


def iterate(matrix):
    """
    Iterates over matrix elements in a generator-style
    Args:
        matrix (np.ndarray): matrix to iterate over

    Yields:
        (int, int, Any): row, column, value
    """
    rows, columns = matrix.shape
    for i in range(0, rows):
        for j in range(columns):
            yield i, j, matrix[i, j]
