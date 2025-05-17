import pandas as pd
import os
import numpy as np

data = {'colA': [1, 2, 3, 4],
        'colB': [10.5, 12.1, np.nan, 15.0],
        'colC': [True, False, True, False]}

df = pd.DataFrame(data)

output_path_csv = 'work_with_file/output.csv'

# Ghi DataFrame ra file CSV
df.to_csv(output_path_csv, sep=',', index=False, header=
          True, na_rep='NULL', float_format='%.2f')

print(f"DataFrame đã được ghi ra file CSV tại {output_path_csv}")

# Ghi ra file TXT với dấu tab và không header/index
output_path_tsv = 'work_with_file/output.txt'
df.to_csv(output_path_tsv, sep='\t', index=False, header=False, na_rep='NULL', float_format='%.2f')
print(f"\nDataFrame đã được ghi ra file TXT tại {output_path_tsv}")