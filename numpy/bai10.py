import numpy as np
x = np.array([[1., 2.], [3., 4.]])
y = np.array([[5., 6.], [7., 8.]])
print("Matrix x:\n", x)
print("Matrix y:\n", y)
 # --- Matrix Multiplication --
# Different from element-wise multiplication (*)
 # Method 1: @ operator (Python 3.5+) - Recommended
dot1 = x @ y
print("\nMatrix multiplication (x @ y):\n", dot1)
 # Method 2: np.dot() function
dot2 = np.dot(x, y)
print("\nMatrix multiplication (np.dot(x, y)):\n", dot2)