import numpy as np

arr = np.arange(10, 20) # Array: [10 11 12 13 14 15 16 17 18 19]
print("Original array:", arr)
 # Indexing (Accessing a single element)
print("Element at index 0:", arr[0])    
print("Element at index 3:", arr[3])     
# Output: 10
 # Output: 13
print("Last element (index -1):", arr[-1])   # Output: 19
 # Slicing (Accessing a section) - [start:stop:step]
print("\nSlice arr[2:5]:", arr[2:5])   # [12 13 14]
print("Slice arr[:4]:", arr[:4])    
# [10 11 12 13]
print("Slice arr[5:]:", arr[5:])    
# [15 16 17 18 19]
print("Slice arr[::2]:", arr[::2])  # [10 12 14 16 18]
 # Assigning values to a slice
arr_copy = arr.copy() # Create a copy to demonstrate view vs copy
arr_copy[5:8] = 99
print("\nAfter assigning arr_copy[5:8] = 99:", arr_copy)
print("\nOriginal array arr afterwards:", arr) # Original array is NOT changed because we used .copy()