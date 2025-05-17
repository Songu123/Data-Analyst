import numpy as np
matrix = np.random.randint(0, 100, size=(5, 4))
print("Matrix origin:", matrix)

row_3 = matrix[2,:]
print("Row 3:", row_3)

last_col = matrix[:,-1]
print("Last column:", last_col)

bottom_rght_2x2 = matrix[-2:,-2:]
print("Bottom right 2x2 submatrix:\n", bottom_rght_2x2)

is_over_50 = matrix > 50

print("Condition (matrix > 50):\n", is_over_50)

elements_over_50 = matrix[is_over_50]
print("Elements greater than 50:", elements_over_50)

matrix_copy = matrix.copy()

matrix_copy[matrix_copy % 2 == 0] = -1

print("\nMatrix after assigning -1 to even elements:\n", matrix_copy)
