import matplotlib.image as mpimg
import numpy as np
from templates import equalization


def rgb2gray(img):
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


#######
# Solution
#######
if __name__ == "__main__":
    # Read the image
    img = mpimg.imread("ej_006.png")

    # Parse the image to a grey-scale with 0 to 1 values
    gray = rgb2gray(img)

    # Create a int-256 matrix
    # This step maybe should NOT be done, and instead
    # allow the templates to resolve a normalized picture
    matrix = gray * 256
    matrix = matrix.astype(int)

    # Solution
    equalization.resolve(matrix, 256, include_ticks=False)
