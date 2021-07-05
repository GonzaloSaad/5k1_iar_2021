import math
from enum import Enum

import numpy as np
from scipy import ndimage


class MaskType(str, Enum):
    PREWITT = "PREWITT"
    SOBEL = "SOBEL"
    GAUSSIAN = "GAUSSIAN"


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

_GAUSS_MASK = [
    [1, 2, 1],
    [2, 8, 2],
    [1, 2, 1],
]


def _gradient(x_gradient, y_gradient):
    return math.sqrt((x_gradient**2) + y_gradient**2)


def _sobel_mask(vicinity):
    y_mask = _Y_AXIS_MASKS[MaskType.SOBEL]
    x_mask = _X_AXIS_MASKS[MaskType.SOBEL]
    y_gradient = sum(sum(vicinity * y_mask))
    x_gradient = sum(sum(vicinity * x_mask))
    return _gradient(x_gradient, y_gradient)


def _prewitt_mask(vicinity):
    y_mask = _Y_AXIS_MASKS[MaskType.PREWITT]
    x_mask = _X_AXIS_MASKS[MaskType.PREWITT]
    y_gradient = sum(sum(vicinity * y_mask))
    x_gradient = sum(sum(vicinity * x_mask))
    return _gradient(x_gradient, y_gradient)


def _gaussian_mask(vicinity):
    return sum(sum(_GAUSS_MASK * vicinity))


_MASKS = {MaskType.PREWITT: _prewitt_mask, MaskType.SOBEL: _sobel_mask, MaskType.GAUSSIAN: _gaussian_mask}


def convolute_py(matrix, mask_type=MaskType.SOBEL):
    return ndimage.gaussian_filter(matrix, sigma=0.5)


def convolute(matrix, mask_type=MaskType.PREWITT):
    convoluted_image = np.full_like(matrix, 0)

    mask = _MASKS[mask_type]

    rows, columns = matrix.shape
    for i in range(0, rows):
        for j in range(columns):

            row_in_range = 0 < i < rows - 1
            column_in_range = 0 < j < columns - 1

            if row_in_range and column_in_range:
                vicinity = matrix[(i - 1):(i + 2), (j - 1):(j + 2)]
                value = mask(vicinity)
            else:
                value = matrix[i, j]

            convoluted_image[i, j] = value

    return convoluted_image
