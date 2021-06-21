from src.image_processing import histogram

#######
# Inputs
#######
grey_scale = 9

matrix_str = """
2 2 3 3 1 8
3 1 4 8 7 4
9 7 5 5 5 6
1 2 3 1 3 2
6 6 7 6 3 3
7 7 8 6 9 6
"""

#######
# Solution
#######
if __name__ == '__main__':
    histogram.resolve(matrix_str, grey_scale)
