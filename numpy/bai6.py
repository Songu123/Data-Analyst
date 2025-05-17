import numpy as np
import os 
 
# if not os.path.exists('data'):
#     os.makedirs('data')
# arr = np.arange(12).reshape(3, 4)
# print("Array to save:\n", arr)
file_path_npy = 'D:/10.Python/Python_Data/numpy/my_array.npy'
# np.save(file_path_npy, arr)
# print(f"Saved to '{file_path_npy}'")

loaded_arr = np.load(file_path_npy)
print("\nArray loaded from .npy file:\n", loaded_arr)