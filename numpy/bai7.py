import numpy as np
 
arr_a = np.array([1, 2, 3])
arr_b = np.linspace(0, 1, 5)
file_path_npz = 'D:/10.Python/Python_Data/numpy/arrays.npz'
 # Save with names 'vec' and 'lin'
np.savez(file_path_npz, vec=arr_a, lin=arr_b)
print(f"\nSaved multiple arrays to '{file_path_npz}'")
 # Load from .npz file (behaves like a dictionary)
archive = np.load(file_path_npz)
print("Loaded array 'vec':", archive['vec'])
print("Loaded array 'lin':", archive['lin'])
print("Keys in file:", list(archive.keys()))
archive.close() # Important to close .npz file after use
 # Use savez_compressed for compression (slower, smaller file)
 # np.savez_compressed('data/arrays_comp.npz', ...)