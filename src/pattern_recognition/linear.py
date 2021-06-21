from io import StringIO

import numpy as np
from numpy import linalg


def get_decision_function_str(w):
    decision_function = StringIO()
    decision_function.write("d(x) = ")
    for i, wi in enumerate(w):
        if not wi:
            continue
        decision_function.write(f"{wi} * x{i + 1}")
        decision_function.write(" + " if i + 1 < len(w) else " ")
    return decision_function.getvalue()


def get_parameter_vector(x, y):
    extended_x = np.array([[*pv, 1] for pv in x])

    x_transposed = np.transpose(extended_x)
    x_transposed_x = np.matmul(x_transposed, extended_x)
    x_transposed_x_inverted = linalg.inv(x_transposed_x)

    w = np.matmul(np.matmul(x_transposed_x_inverted, x_transposed), y)
    w = np.round(w)
    return w
