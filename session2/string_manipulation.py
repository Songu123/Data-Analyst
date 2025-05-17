import pandas as pd
import numpy as np

data = {'TextCol': ['Hello', ' World ', 'Python Data Analyst', np.nan, 'Pandas', '123']}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Áp dụng phương thức chuỗi thông qua .str
# Chuyển sang chữ thường và xoá khoảng trắng thừa hai đầu
df['TextCol_clean'] = df['TextCol'].str.lower().str.strip()
print("\nCleaned TextCol:\n", df['TextCol_clean'])

# Kiểm tra chứa chuỗi con
df['Contains_Data'] = df['TextCol_clean'].str.contains('data', na=False)
print("\n.str.contains('data'):\n", df)

# Thay thế chuỗi con
df['TextCol_Replaced'] = df['TextCol_clean'].str.replace('world', 'everyone', case=False)
print("\n.str.replace('world', 'everyone'):\n", df)

# Tách chuỗi (trả về Series of lists)
df['TextCol_Split'] = df['TextCol_clean'].str.split(' ')
print("\nSplit TextCol:\n", df)