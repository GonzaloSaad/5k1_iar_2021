from src.image_processing import equalization

#######
# Inputs
#######
grey_scale = 15

matrix_str = """
8 5 5 5 8 8 5 5 5 8
5 2 2 5 5 5 2 2 5 8
5 4 4 2 5 2 5 2 5 8
5 4 4 4 2 5 5 5 5 8
5 5 4 4 4 5 5 5 5 8
8 5 5 4 4 5 5 5 5 8
8 8 5 5 5 5 5 8 8 8
8 8 8 8 8 8 8 8 8 8
"""

#######
# Solution
#######
if __name__ == '__main__':
    equalization.resolve(matrix_str, grey_scale)
