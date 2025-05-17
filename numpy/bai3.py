import numpy as np
arr2d = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
print("Original 2D array:\n", arr2d)
# Access element at row 1, column 2
element = arr2d[1, 2]
print("\nElement arr2d[1, 2]:", element) # Output: 6
# Get entire row 0 (axis 0, index 0)
row0 = arr2d[0] # or arr2d[0, :]
print("\nHàng 0 (arr2d[0]):", row0, row0.shape) # Output: [1 2 3] (1D array
 # Slicing on both dimensions: Get top 2 rows, last 2 columns
sub_array = arr2d[:2, 1:]
print(arr2d[:,:])
print("\nSlice top 2 rows, last 2 cols (arr2d[:2, 1:]):\n", sub_array)
 # Output: [[2 3]
 #          [5 6]]
 # Assign values to a 2D slice (modifies original array!)
arr2d_view_test = arr2d # Another view
arr2d_view_test[1, :2] = 0 # Assign 0 to the first 2 elements of row 1
print("\nAfter assigning arr2d_view_test[1, :2] = 0:")
print("arr2d_view_test:\n", arr2d_view_test)
print("Original arr2d IS CHANGED:\n", arr2d) # Original array is also changed