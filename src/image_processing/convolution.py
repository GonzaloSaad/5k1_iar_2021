from enum import Enum

import numpy as np


class MaskType(str, Enum):
    PREWITT = "PREWITT"
    SOBEL = "SOBEL"


_MASKS = {
    MaskType.PREWITT: np.array([
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1],
    ]),
    MaskType.SOBEL: np.array([
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1],
    ]),
}


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
                value = sum(sum(vicinity * mask))
            else:
                value = matrix[i, j]

            convoluted_image[i, j] = value

    return convoluted_image
