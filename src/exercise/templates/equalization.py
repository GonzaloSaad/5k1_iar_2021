import matplotlib.pyplot as plt
import numpy as np

from src import matrix as m


def resolve(matrix_str, grey_scale):
    matrix = m.from_str(matrix_str)
    elements = m.get_elements(matrix)

    # Histogram
    histogram, histogram_norm = m.histogram(matrix, grey_scale)

    print("\tg\tf(g)\th(g)")
    for i in range(0, grey_scale + 1):
        print(f"\t{i}\t{histogram[i]}\t\t{histogram_norm[i]}")

    # Equalization
    histogram_eq = np.zeros(grey_scale + 1)
    for i in range(0, grey_scale):
        delta_g_first = grey_scale * histogram_norm[i]
        g_first = delta_g_first + histogram_eq[i - 1] if i > 0 else delta_g_first
        histogram_eq[i] = g_first

    matrix_eq = np.zeros(matrix.shape)
    for i in range(0, len(matrix)):
        row = matrix[i]
        for j in range(0, len(row)):
            g = matrix[i, j]
            g_eq = histogram_eq[g]
            matrix_eq[i, j] = g_eq

    # Display
    bins = np.arange(0, grey_scale + 1.5) - 0.5
    ticks = np.arange(0, grey_scale + 2)

    fig, axs = plt.subplots(2, 2)

    for ax in axs[0]:
        ax.set_xticks(ticks)
        ax.set_xlabel("Intensity")
        ax.set_ylabel("Frequency")

    matrix_ax = axs[0, 0]
    matrix_ax.set_title("Histogram of Matrix")
    matrix_ax.hist(elements, bins=bins, rwidth=0.5, align="mid", edgecolor="black")

    matrix_img_ax = axs[1, 0]
    matrix_img_ax.get_xaxis().set_visible(False)
    matrix_img_ax.get_yaxis().set_visible(False)
    matrix_img_ax.imshow(matrix, cmap="gray_r", vmin=0, vmax=grey_scale)

    eq_elements = m.get_elements(matrix_eq)
    matrix_eq_ax = axs[0, 1]
    matrix_eq_ax.set_title("Histogram of Equalized Matrix")
    matrix_eq_ax.hist(eq_elements, bins=bins, rwidth=0.5, align="mid", edgecolor="black")

    matrix_eq_img_ax = axs[1, 1]
    matrix_eq_img_ax.get_xaxis().set_visible(False)
    matrix_eq_img_ax.get_yaxis().set_visible(False)
    matrix_eq_img_ax.imshow(matrix_eq, cmap="gray_r", vmin=0, vmax=grey_scale)

    fig.tight_layout()
    plt.show()
