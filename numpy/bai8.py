
import numpy as np
 # (Assume 'data' directory exists)
arr = (np.arange(6).reshape(2, 3) + 1) * 1.25
print("Array to save (text):\n", arr)
file_path_csv = 'D:/10.Python/Python_Data/numpy/my_array.csv'
np.savetxt(file_path_csv, arr,
delimiter=',',    
fmt='%.3f',       
# Column delimiter
 # Float format
header='Col1,Col2,Col3', # Header row
comments='# ')     
# Comment character
print(f"\nSaved to '{file_path_csv}'")