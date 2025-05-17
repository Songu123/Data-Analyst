import pandas as pd
import os

file_path = "work_with_file/thuchanh1.csv"

#Tao file gia
if not os.path.exists('data'): os.makedirs('data')
csv_content="""colA,colB,colC
1,10.5,True
2,12.1,False
3,,True
4,15.0,False"""
with open(file_path, 'w') as f:
    f.write(csv_content)

# Đọc file CSV vào DataFrame
df_csv = pd.read_csv(file_path, delimiter=',', header=0, index_col=None, skiprows=0,na_values=[''], dtype={'colA': 'int', 'colB': 'float', 'colC': 'bool'})
print("DataFrame từ file CSV:\n", df_csv)