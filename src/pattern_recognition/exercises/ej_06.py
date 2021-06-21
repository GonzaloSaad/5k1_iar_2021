from io import StringIO

import numpy as np
from numpy import linalg

from src.image import plot_function
from src.pattern_recognition import linear

#################
# Inputs
#################


def main():
    x = [
        [0, 0],
        [1, 0],
        [2, 0],
        [0, 1],
        [1, 1],
        [2, 1],
    ]

    y = [
        1,
        1,
        1,
        -1,
        -1,
        -1,
    ]

    w = linear.get_parameter_vector(x, y)

    m = w[0] / w[1]
    b = -(w[2] / w[1])

    def decision_function(x2):
        return m * x2 + b

    decision_function_str = linear.get_decision_function_str(w)
    plot_function(decision_function, xlabel="x2", ylabel="x1", title=decision_function_str)


if __name__ == '__main__':
    main()
