import numpy as np 
import pandas as pd 
# Dữ liệu cho NumPy 
list_data_np_large = [ 
[10, 15, 20, 25, 30, 35], 
[40, 45, 50, 55, 60, 65], 
[70, 75, 80, 85, 90, 95], 
[100, 105, 110, 115, 120, 125], 
[130, 135, 140, 145, 150, 155], 
[160, 165, 170, 175, 180, 185], 
[190, 195, 200, 205, 210, 215], 
[220, 225, 230, 235, 240, 245], 
[250, 255, 260, 265, 270, 275], 
[280, 285, 290, 295, 300, 305] 
] 
# Dữ liệu cho Pandas DataFrame 
data_students_large = { 
'Mã SV': [f'SV{i:03d}' for i in range(1, 31)], 
'Tên': [ 
'Nguyễn Văn A', 'Trần Thị B', 'Lê Văn C', 'Phạm Thị D', 'Hoàng Văn E', 
'Phan Thị F', 'Vũ Văn G', 'Đặng Thị H', 'Bùi Văn I', 'Đỗ Thị K', 
'Nguyễn Văn L', 'Trần Thị M', 'Lê Văn N', 'Phạm Thị O', 'Hoàng Văn P', 
'Phan Thị Q', 'Vũ Văn R', 'Đặng Thị S', 'Bùi Văn T', 'Đỗ Thị U', 
'Trần Văn V', 'Lê Thị W', 'Phạm Văn X', 'Hoàng Thị Y', 'Bùi Văn Z', 
'Đỗ Thị AA', 'Nguyễn Văn BB', 'Trần Thị CC', 'Lê Văn DD', 'Phạm Thị EE' 
], 
'Điểm Toán': [ 
8.5, 7.0, 9.0, 6.5, 8.0, 7.8, 9.2, 6.0, 8.8, 7.5, 
np.nan, 8.1, 7.3, 9.5, 6.8, 8.9, 7.1, 9.8, 6.2, 8.4, 
7.9, 8.6, np.nan, 9.1, 6.7, 8.3, 7.6, 9.4, 6.9, 8.7 
], 
'Điểm Lý': [ 
7.5, 8.0, 8.5, 7.0, 7.5, 8.2, 7.8, 6.5, 8.5, 7.0, 
8.8, np.nan, 7.6, 9.0, 7.2, 8.7, 7.4, 9.3, 6.7, 8.0, 
7.9, 8.1, 7.3, np.nan, 7.7, 8.4, 7.5, 9.2, 6.8, 8.5 
], 
'Điểm Hóa': [ 
9.0, 7.5, 8.0, 6.0, 8.5, 8.8, 9.5, 5.5, 9.2, 8.0, 
8.1, 7.9, np.nan, 9.8, 7.0, 9.1, 7.7, 9.9, 6.5, 8.6, 
8.9, 7.8, 8.2, 6.3, np.nan, 8.5, 7.1, 9.7, 6.6, 8.8 
], 
'Giới tính': [ 
'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 
'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 
'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ' 
], 
'Thành phố': [ 
'HN', 'HCM', 'ĐN', 'HN', 'HP', 'HCM', 'ĐN', 'HN', 'HP', 'HCM', 
'HN', 'ĐN', 'HP', 'HCM', 'ĐN', 'HN', 'HP', 'HCM', 'ĐN', 'HN', 
'HCM', 'ĐN', 'HN', 'HP', 'HCM', 'ĐN', 'HN', 'HP', 'HCM', 'ĐN' 
], 
'Số buổi vắng': [ 
0, 1, 0, 2, 1, 0, 0, 3, 1, 0, 
1, 0, 2, 0, 1, 0, 0, 0, 2, 1, 
0, 1, 0, 0, 1, 0, 2, 1, 0, 0 
] 
} 

# Câu 6 (1 điểm): Sử dụng DataFrame data_students_large đã tạo ở Bài kiểm tra số 1. Đếm 
# và in ra số lượng giá trị thiếu (NaN) trong mỗi cột của DataFrame. Sau đó, điền giá trị 
# thiếu trong cột 'Điểm Lý' bằng giá trị trung bình của toàn bộ cột 'Điểm Lý', và điền giá 
# trị thiếu trong cột 'Điểm Toán' bằng giá trị trung vị của toàn bộ cột 'Điểm Toán'. In 5 
# hàng đầu tiên của DataFrame sau khi điền. 
df = pd.DataFrame(data_students_large)

print("DataFrame ban đầu:\n", df)

print("Số lượng giá trị thiếu (NaN) trong mỗi cột:\n", df.isna().sum())

print("\nĐiền giá trị thiếu trong cột 'Điểm Lý' bằng giá trị trung bình:")
df['Điểm Lý'] = df['Điểm Lý'].fillna(df['Điểm Lý'].mean())

# Điền giá trị thiếu trong cột 'Điểm Toán' bằng trung vị
df['Điểm Toán'] = df['Điểm Toán'].fillna(df['Điểm Toán'].median())

# In 5 hàng đầu tiên
print("\n5 hàng đầu tiên sau khi điền NaN:\n", df.head(5))

# Câu 7 (1 điểm): Tiếp tục sử dụng DataFrame từ Câu 6. Điền các giá trị thiếu còn lại 
# trong cột 'Điểm Hóa' bằng giá trị trung vị của cột 'Điểm Hóa' trong từng nhóm 'Giới 
# tính' tương ứng. Sử dụng phương thức transform(). In 5 hàng đầu tiên của DataFrame 
# sau khi điền. 

df['Điểm Hóa'] = df.groupby('Giới tính')['Điểm Hóa'].transform(lambda x: x.fillna(x.median()))
print("\n5 hàng đầu tiên sau khi điền NaN trong cột 'Điểm Hóa':\n", df.head(5))

# Câu 8 (1 điểm): Tiếp tục sử dụng DataFrame từ Câu 7 (lúc này các cột điểm không 
# còn NaN). Tạo một cột mới tên là 'Tổng điểm 3 môn' là tổng của các cột 'Điểm Toán', 
# 'Điểm Lý' và 'Điểm Hóa'. In 5 hàng đầu tiên của DataFrame bao gồm cột mới này. 
df['Tổng điểm 3 môn'] = df[['Điểm Toán', 'Điểm Lý', 'Điểm Hóa']].sum(axis=1)
print("\n5 hàng đầu tiên của DataFrame với cột 'Tổng điểm 3 môn':\n", df[['Mã SV', 'Tổng điểm 3 môn']].head(5))

# Câu 9 (1 điểm): Sử dụng DataFrame từ Câu 8. Phân nhóm DataFrame theo cột 'Thành 
# phố'. Đối với mỗi thành phố, tính và in ra giá trị trung bình của cột 'Tổng điểm 3 môn' 
# và tổng của cột 'Số buổi vắng'.
grouped_df = df.groupby('Thành phố').agg({'Tổng điểm 3 môn': 'mean', 'Số buổi vắng': 'sum'})
print("\nGiá trị trung bình của 'Tổng điểm 3 môn' và tổng của 'Số buổi vắng' theo từng thành phố:\n", grouped_df)

# Câu 10 (1 điểm): Sử dụng DataFrame từ Câu 8. Tạo một Pivot Table hiển thị giá trị 
# trung bình của cột 'Số buổi vắng'. Đặt cột 'Thành phố' làm index (các hàng) và cột 
# 'Giới tính' làm columns (các cột). Điền các giá trị thiếu (nếu có) trong Pivot Table bằng 
# giá trị -1. In Pivot Table kết quả. 
pivot_table = df.pivot_table(values='Số buổi vắng', index='Thành phố', columns='Giới tính', aggfunc='mean')
pivot_table = pivot_table.fillna(-1)
print("\nPivot Table với giá trị trung bình của 'Số buổi vắng':\n", pivot_table)