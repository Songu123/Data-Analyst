import pandas as pd
import numpy as np

data = {
 'A': [1, 2, np.nan, 4, 5],
 'B': [6, np.nan, 8, 9, 10],
 'C': [11, 12, 13, np.nan, np.nan],
 'D': ['X', 'Y', np.nan, 'X', 'Z'] # Cột chuỗi
 }

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

print("Count nun\n:", df.isnull().sum())

print("Delete row with NaN:\n", df.dropna())

df_filled_const = df.fillna(0)
print("\n Dien Nan bang 0:\n", df_filled_const)

# Cách 1: Điền bằng giá trị thống kê (chỉ cột số)
mean_A = df['A'].mean()
df['A'] = df['A'].fillna(mean_A)
print("\n Dien NaN cot A bang mean:\n", df)

# Điền bằng giá trị phổ biến nhất (mode) (thường cho cột phân loại)
mode_D = df['D'].mode()[0] # .mode() trả về Series, lấy phần tử đầu tiên
df['D'] = df['D'].fillna(mode_D)
print("\nĐiền NaN cột 'D' bằng Mode:\n", df)

# Cách 3: Điền bằng phương pháp nội suy (interpolation)
df['C'] = df['C'].interpolate() 
print("\n Dien NaN cot C bang phuong phap noi suy:\n", df)

# Cách 4: Điền bằng phương pháp forward fill (ffill)
df_ffill = df.fillna(method='ffill')
print("\n Dien NaN bang phuong phap forward fill:\n", df_ffill)