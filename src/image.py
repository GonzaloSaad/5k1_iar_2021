import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def _rgb2gray(img):
    """
    Performs the dot product between the RGB component of
    each pixel of the image with an specific array

    Taken from the Pillow library
        - https://pillow.readthedocs.io/en/3.2.x/reference/Image.html#PIL.Image.Image.convert


    Args:
        img: The image to convert

    Returns:
        np.ndarray: the grey scale image
    """
    return np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])


def read(name, convert_to_grey=True):
    # Read the image
    img = mpimg.imread(name)

    # Parse the image to a grey-scale with 0 to 1 values
    if convert_to_grey:
        return _rgb2gray(img)
    return img


def display(*imgs, grey_scale=True, grey_scale_range=256, reverse_grey=True):
    fig, axs = plt.subplots(1, len(imgs))

    if not isinstance(axs, np.ndarray):
        axs = [axs]

    for i, img in enumerate(imgs):
        ax = axs[i]

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        if grey_scale:
            cmap = "gray_r" if reverse_grey else "gray"
            ax.imshow(img, cmap=cmap, vmin=0, vmax=grey_scale_range)
        else:
            ax.imshow(img)

    fig.tight_layout()
    plt.show()


def as_binary(matrix, grey_scale, threshold=None):
    """
    Transforms a matrix to a binary one
    Args:
        matrix (np.ndarray):
        grey_scale (int): maximum value of a pixel
        threshold (int): value to use for decide if an element is present or not

    Returns:
        np.ndarray: binary matrix
    """
    threshold = threshold or grey_scale // 2

    binary_image = np.full_like(matrix, 0)
    rows, columns = matrix.shape
    for i in range(0, rows):
        for j in range(columns):

            if matrix[i, j] > threshold:
                binary_image[i, j] = grey_scale

    return binary_image
