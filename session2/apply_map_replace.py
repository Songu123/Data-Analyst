import pandas as pd
import numpy as np

data = {'Value': [10,20,30,40,50],
        'Category': ['A', 'B', 'C', 'A', 'B'],
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
        'Text': ['Hello', 'World', 'Pandas', 'Python', 'DataFrame']}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Áp dụng hàm lên Series (.apply())
# Bình phương mỗi giá trị
df['Value_Sq'] = df['Value'].apply(lambda x: x**2)
print("\nApply: Bình phương cột 'Value':\n", df)


# Ví dụ: Áp dụng hàm phức tạp hơn (viết hàm riêng)
def map_category_to_label(category):
    if category == 'A':
        return 'Alpha'
    elif category == 'B':
        return 'Beta'
    elif category == 'C':
        return 'Gamma'
    else:
        return 'Unknown'
df['Category_Label'] = df['Category'].apply(map_category_to_label)
print("\nApply: Chuyển đổi cột 'Category' sang nhãn:\n", df)

# Áp dụng hàm lên Dataframe (theo hàng hoặc cột)
# Mặc định axis=0 (áp dụng lên mỗi cột)
df_col_sums = df[['Value_Sq']].apply(sum)
axis = 1
def summarize_row(row):
    return f"{row['Category']}: {row['Value']}"
df['Summary'] = df.apply(summarize_row, axis=1)

print("\nApply: Tóm tắt mỗi hàng:\n", df[['Category', 'Value', 'Summary']])

# Ánh xạ giá trị (.map()) - Chỉ áp dụng Series
# Tương tự apply cho Series nhưng thường dùng với dictionary hoặc Series mapping
status_map = {'A': 'Active', 'B': 'Inactive', 'C': 'Pending'}
df['Status'] = df['Category'].map(status_map)
print("\nMap: Ánh xạ cột 'Category' sang 'Status':\n", df[['Category', 'Status']])

# Thay thế giá trị (.replace()) - Áp dụng cho Series hoặc DataFrame
# Thay thế 20 bằng 200 trong cột 'Value'
df['Value'] = df['Value'].replace(20, 200)
print("\nReplace: Thay thế 20 bằng 200 trong cột 'Value':\n", df[['Value']])