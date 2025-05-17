import pandas as pd
import numpy as np
data = {
   'Product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse', 'Keyboard'],
   'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
   'Sales': [1000, 150, 75, 1200, 180, 90],
   'Quantity': [10, 5, 3, 12, 6, 4]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
 # Tạo Pivot Table: Tổng Sales theo Region và Product
 # index: cột dùng làm index (hàng)
 # columns: cột dùng làm cột mới
 # values: cột chứa giá trị cần tổng hợp
 # aggfunc: hàm tổng hợp (mặc định 'mean')
pivot_sales = pd.pivot_table(df,
                            index='Region',
                            columns='Product',
                            values='Sales',
                            aggfunc='sum')
print("\nPivot Table: Tổng Sales theo Region và Product:\n", pivot_sales)
 # Pivot Table với nhiều values và nhiều aggfunc
pivot_multi = pd.pivot_table(df,
                            index='Region',
                            columns='Product',
                            values=['Sales', 'Quantity'],
                            aggfunc={'Sales': 'sum', 'Quantity': 'mean'})
print("\nPivot Table: Tổng Sales, Trung bình Quantity:\n", pivot_multi)
 # Pivot Table với fill_value (điền NaN) và margins (tính tổng cộng)
pivot_margins = pd.pivot_table(df,
                             index='Region',
                             columns='Product',
                             values='Sales',
                             aggfunc='sum')
