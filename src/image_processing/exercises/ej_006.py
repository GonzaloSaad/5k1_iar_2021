from src import image
from src.image_processing import equalization

#######
# Solution
#######
if __name__ == "__main__":
    image_name = "../images/ej_006.png"

    # Read the image
    img = image.read(image_name)
    # Create a int-256 matrix
    # This step maybe should NOT be done, and instead
    # allow the templates to resolve a normalized picture
    matrix = img * 256
    matrix = matrix.astype(int)

    # Solution
    equalization.resolve(matrix, 256, include_ticks=False)
