from src.image_processing import equalization

#######
# Inputs
#######
grey_scale = 8

matrix_str = """
4 5 5 7
7 5 7 8
4 5 6 5
8 6 5 7
"""

#######
# Solution
#######
if __name__ == '__main__':
    equalization.resolve(matrix_str, grey_scale)
