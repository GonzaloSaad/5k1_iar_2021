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

    # Display
    bins = np.arange(0, grey_scale + 1.5) - 0.5
    ticks = np.arange(0, grey_scale + 2)

    fig, axs = plt.subplots(1, 2)

    matrix_ax = axs[0]
    matrix_ax.set_title("Histogram of Matrix")
    matrix_ax.set_xticks(ticks)
    matrix_ax.set_xlabel("Intensity")
    matrix_ax.set_ylabel("Frequency")
    matrix_ax.hist(elements, bins=bins, rwidth=0.5, align="mid", edgecolor="black")

    matrix_img_ax = axs[1]
    matrix_img_ax.imshow(matrix, cmap="gray", vmin=0, vmax=grey_scale)
    matrix_img_ax.get_xaxis().set_visible(False)
    matrix_img_ax.get_yaxis().set_visible(False)

    fig.tight_layout()
    plt.show()
