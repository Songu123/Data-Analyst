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


# Câu 1 (1 điểm): Tạo một NumPy array 2 chiều từ list_data_np_large. In ra array vừa 
# tạo, kích thước (shape), số chiều (ndim) và kiểu dữ liệu (dtype) của nó. 
array_np = np.array(list_data_np_large)

print("Array 2 chiều:\n", array_np)
print("Kích thước (shape):", array_np.shape)
print("Số chiều (ndim):", array_np.ndim)
print("Kiểu dữ liệu (dtype):", array_np.dtype)

# Câu 2 (1 điểm): Tạo một NumPy array 1 chiều chứa 12 phần tử cách đều nhau trong 
# khoảng từ -5 đến 5 (bao gồm cả hai đầu). In array này. 
array_1d = np.linspace(-5, 5, 12)

print("\nArray 1 chiều:\n", array_1d)

# Câu 3 (1 điểm): Từ mảng 2 chiều tạo ở Câu 1, trích xuất và in ra ma trận con gồm 3 
# hàng đầu tiên và 4 cột cuối cùng. 
sub_array = array_np[:3, -4:]
print("\nMa trận con (3 hàng đầu tiên và 4 cột cuối cùng):\n", sub_array)



# Câu 4 (1 điểm): Tạo một Pandas DataFrame từ dictionary data_students_large. In 7 
# hàng đầu tiên và 5 hàng cuối cùng của DataFrame. 
df_students = pd.DataFrame(data_students_large)
print("\n7 hàng đầu tiên của DataFrame:\n", df_students.head(7))
print("\n5 hàng cuối cùng của DataFrame:\n", df_students.tail(5))

# Câu 5 (1 điểm): Từ DataFrame tạo ở Câu 4, chọn và in ra chỉ các cột 'Mã SV', 'Tên' và 
# 'Giới tính'. 
selected_columns = df_students[['Mã SV', 'Tên', 'Giới tính']]
print("\nChỉ các cột 'Mã SV', 'Tên' và 'Giới tính':\n", selected_columns)


