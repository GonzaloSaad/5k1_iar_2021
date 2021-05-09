from enum import Enum
from statistics import mean, median

import numpy as np


class FilterType(str, Enum):
    MEAN = "MEAN"
    MEDIAN = "MEDIAN"


def filter_image(matrix, vicinity, filter_type):
    """
    Applies a filter on a given image

    Args:
        matrix: ndarray representing a grey-scale  image
        vicinity: tuple representing the vicinity
        filter_type: type of the filter to apply

    Returns:
        ndarray: filtered image
    """
    filtered_matrix = np.full_like(matrix, 0)

    rows, columns = matrix.shape
    v_row, v_col = vicinity

    filter_func = mean if filter_type == FilterType.MEAN else median
    for i in range(0, rows):
        for j in range(columns):

            row_out_of_range = i < (v_row - 1) or (i + v_row) > rows
            column_out_of_range = j < (v_col - 1) or (j + v_col) > columns

            if row_out_of_range or column_out_of_range:
                value = matrix[i, j]
            else:
                value = filter_func(matrix[i, (j - v_col + 1):j + 1])

            filtered_matrix[i, j] = value

    return filtered_matrix
