import matplotlib.image as mpimg
import numpy as np
from templates import equalization, histogram

#######
# Inputs
#######


def rgb2gray(img):
    """
    Performs the dot product between the RGB component of
    each pixel of the image with an specific array

    Taken from the Pillow library
        - https://pillow.readthedocs.io/en/3.2.x/reference/Image.html#PIL.Image.Image.convert


    Args:
        rgb: The image to convert

    Returns:
        np.ndarray: the grey scale image
    """
    return np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])


#######
# Solution
#######
if __name__ == "__main__":

    # Read the image
    img = mpimg.imread("ej_006.png")
    gray = rgb2gray(img)

    matrix = gray * 256
    matrix = matrix.astype(int)
    equalization.resolve(matrix, 256, include_ticks=False)
