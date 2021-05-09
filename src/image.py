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


def display(*imgs, grey_scale=True, grey_scale_range=256):
    fig, axs = plt.subplots(1, len(imgs))

    if not isinstance(axs, np.ndarray):
        axs = [axs]

    for i, img in enumerate(imgs):
        ax = axs[i]

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        if grey_scale:
            ax.imshow(img, cmap="gray_r", vmin=0, vmax=grey_scale_range)
        else:
            ax.imshow(img)

    fig.tight_layout()
    plt.show()
