from src import image
from src.image_processing import filters
from src.image_processing.filters import FilterType

#######
# Solution
#######
if __name__ == "__main__":
    image_name = "../images/ej_014.png"

    img = image.read(image_name)
    matrix = img * 256
    matrix = matrix.astype(int)

    vicinity = (10, 20)
    filter_type = FilterType.MEDIAN

    filtered_matrix = filters.filter_image(matrix, vicinity, filter_type)

    image.display(matrix, filtered_matrix)
