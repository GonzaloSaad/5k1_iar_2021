import math
from enum import Enum

import numpy as np
from scipy import ndimage


class MaskType(str, Enum):
    PREWITT = "PREWITT"
    SOBEL = "SOBEL"


_X_AXIS_MASKS = {
    MaskType.PREWITT: np.array([
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1],
    ]),
    MaskType.SOBEL: np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1],
    ]),
}

_Y_AXIS_MASKS = {
    MaskType.PREWITT: np.array([
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1],
    ]),
    MaskType.SOBEL: np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1],
    ]),
}


def convolute_py(matrix, mask_type=MaskType.SOBEL):
    return ndimage.sobel(matrix)


def convolute(matrix, mask_type=MaskType.PREWITT):
    convoluted_image = np.full_like(matrix, 0)

    x_mask = _X_AXIS_MASKS[mask_type]
    y_mask = _Y_AXIS_MASKS[mask_type]

    rows, columns = matrix.shape
    for i in range(0, rows):
        for j in range(columns):

            row_in_range = 0 < i < rows - 1
            column_in_range = 0 < j < columns - 1

            if row_in_range and column_in_range:
                vicinity = matrix[(i - 1):(i + 2), (j - 1):(j + 2)]
                y_gradient = sum(sum(vicinity * y_mask))
                x_gradient = sum(sum(vicinity * x_mask))
                value = math.sqrt((x_gradient**2) + y_gradient**2)
            else:
                value = matrix[i, j]

            convoluted_image[i, j] = value

    return convoluted_image
