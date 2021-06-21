from src import image
from src.image_processing import convolution
from src.image_processing.convolution import MaskType

_IMAGES = [
    "../images/ej_018_0.png",
    "../images/ej_018_1.png",
]

#######
# Solution
#######
if __name__ == "__main__":
    for img_name in _IMAGES:
        img = image.read(img_name)
        matrix = img * 256
        matrix = matrix.astype(int)

        convoluted_matrix = convolution.convolute(matrix, mask_type=MaskType.PREWITT)

        image.display(matrix, convoluted_matrix, reverse_grey=False)

        print("Siguiente")
        input()
