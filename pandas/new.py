
import pandas as pd

# cau1
population = pd.Series([8.3, 9.0, 1.1], index=["Hanoi", "HCM City", "Danang"])
print("Population Series:\n", population)

# cau2
data = {
    'city': ['Hanoi', 'HCM City', 'Danang', 'Haiphong'],       
    'province': ['Hanoi', 'HCM', 'Danang', 'Haiphong'],
    'area_sq_km': [3359, 2095, 1285, 1520],
    'population_mil': [8.3, 9.0, 1.1, 2.1]
}

city_data = pd.DataFrame(data, index=['one', 'two', 'three', 'four'])
print("\nCity DataFrame:\n", city_data)

# cau3
print("\nDữ liệu 2 hàng đầu tiên:\n", city_data.head(2))
population_col = city_data['population_mil']

# cau4
print("\nPopulation_mil column:\n", population_col)

# cau5
city_province = city_data[['province', 'city']]
print("\nCity and Province columns:\n", city_province)

# cau6
try:
    # Using string index 'three' instead of numeric 2
    row_loc = city_data.loc['three']
    print("\nRow at index 'three':\n", row_loc)
except KeyError as e:
    print(f"\nError accessing row: {e}")

# cau7
try:
    row_iloc = city_data.iloc[1]
    print("\nRow at position 1 using iloc:\n", row_iloc)
except IndexError as e:
    print(f"\nError accessing row: {e}")

# cau8
try:
    # Using string indices for loc
    subset_loc = city_data.loc['two':'four', ['city', 'population_mil']]
    print("\nSubset using loc:\n", subset_loc)
except KeyError as e:
    print(f"\nError creating subset: {e}")

# cau9
large_cities = city_data[city_data['population_mil'] > 5]
print("\nCities with population > 5 million:\n", large_cities)

# cau10
try:
    # Using string index 'one' instead of numeric 0
    drop_city = city_data.drop('one')
    print("\nDataFrame after dropping row 'one':\n", drop_city)
except KeyError as e:
    print(f"\nError dropping row: {e}")
