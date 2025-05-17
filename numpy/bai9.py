import numpy as np
file_path_csv = 'D:/10.Python/Python_Data/numpy/my_array.csv'

# loadtxt: Simple, fast, but fragile with missing/malformed data
try:
    loaded_txt = np.loadtxt(file_path_csv, delimiter=',', skiprows=1)
    print("\nLoaded from text (loadtxt):\n", loaded_txt)
except Exception as e:
    print("\nloadtxt Error:", e)
 # genfromtxt: More flexible, handles missing data
loaded_gen = np.genfromtxt(file_path_csv, delimiter=',',
skip_header=1,
filling_values=np.nan) # Fill missing with NaN
print("\nTải từ text (genfromtxt):\n", loaded_gen)