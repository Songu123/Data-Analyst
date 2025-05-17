import pandas as pd

data = {'old_col_name_1': [1, 2, 3],
        'old_col_name_2': [4, 5, 6],}

df = pd.DataFrame(data, index = ['row_a', 'row_b', 'row_c'])

print("Original DataFrame:\n", df)

df_renamed_cols = df.rename(columns={'old_col_name_1': 'new_col_A',
                            'old_col_name_2': 'new_col_B'})

print("\nDataFrame with renamed columns:\n", df_renamed_cols)

# Đổi tên index hàng (dùng dictionary mapping)
 # df.rename(index={'nhãn_cũ': 'nhãn_mới', ...})

df_renamed_index = df.rename(index={'row_a': 'alpha',
                                  'row_b': 'beta',
                                  'row_c': 'new_row_c'})
print("\nDataFrame with renamed index:\n", df_renamed_index)
# Đổi tên index hàng (dùng list)

df_renamed_all = df.rename(columns={'old_col_name_1': 'Col_1'},
 index={'row_c': 'gamma'})

print("\nDataFrame with renamed columns and index:\n", df_renamed_all)
