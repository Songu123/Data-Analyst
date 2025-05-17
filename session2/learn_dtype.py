import pandas as pd
import numpy as np

data = {'IntCol': [1, 2, 3, 4],
        'FloatCol': [1.1, 2.2, 3.3, 4.4],
        'StringCol': ['10', '20', '30', '40'],
        'BoolCol': [True, False, True, False],
        'DateStrCol': ['2023-01-01', '2203-01-30', '2023-01-03', '2023-01-04'],
        'NumericWithErr': ['1', '2', 'error', '4']
        }

df = pd.DataFrame(data)
print("\nDataFrame dtypes:\n", df.dtypes)

# Chuyển đổi kiểu dữ liệu bằng astype()
df['IntCol'] = df['IntCol'].astype(float)
df['FloatCol'] = df['FloatCol'].astype(int)
df['StringCol'] = df['StringCol'].astype(int)

print("\nDataFrame after astype():\n", df.dtypes)
print(df)

# Chuyển đồi sang kiểu datetime (Quan trọng cho dữ liệu thời gian)
df['DateStrCol'] = pd.to_datetime(df['DateStrCol'])
print("\nDataFrame after converting DateStrCol to datetime:\n", df.dtypes)
print(df)

# Chuyển đổi sang kiểu số (Xử lý lỗi: errors = 'coerce' chuyển lỗi thành NaN)
df['NumericWithErr'] = pd.to_numeric(df['NumericWithErr'], errors='coerce')
df['DateStrCol'] = pd.to_datetime(df['DateStrCol'], errors='coerce')
print("\nDataFrame sau khi dùng pd.to_numeric:\n", df.dtypes)
print(df)

#Chuyển đổi sang kiểu category 
df['CategoryCol'] = df['StringCol'].astype('category')

print(df)