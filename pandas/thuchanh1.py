import pandas as pd

# cau1
population = pd.Series([8.3, 9.0, 1.1], index=["Hanoi", "HCM City", "Danang"])
print("Population Series:\n", population)

# cau2
data = {'city': ['Hanoi', 'HCM City', 'Danang', 'Haiphong'],       
'province': ['Hanoi', 'HCM', 'Danang', 'Haiphong'],
'area_sq_km': [3359, 2095, 1285, 1520],
 'population_mil': [8.3, 9.0, 1.1, 2.1]}

city_data = pd.DataFrame(data)
print("\nCity DataFrame:\n", city_data)

# cau3
print("Dữ liệu 2 hàng đầu tiên:\n", city_data.head(2))
population_col = city_data['population_mil']

# cau4
print("Population_mil column:\n", population_col)

# cau5
city_province = city_data[['province', 'city']]
print("City and Province columns:\n", city_province)

# cau6
row_loc = city_data.loc[2]
print("Row at index 2:\n", row_loc)

# cau7
row_iloc = city_data.iloc[1]
print("Row at index 1 using iloc:\n", row_iloc)

# cau8
subset_loc = city_data.loc[1:3, ['city', 'population_mil']]
print("Subset using loc:\n", subset_loc)

# cau9
large_cities = city_data[city_data['population_mil']> 5]
print("Cities with population > 5 million:\n", large_cities)

# cau10
drop_city = city_data.drop(0)
print("DataFrame after dropping row 0:\n", drop_city)



# THUCHANH 2
city_data["density_per_sq_km"] = city_data['population_mil'] / city_data['area_sq_km']
print("\nCity DataFrame with density:\n", city_data)

city_with_max_pop = city_data.loc[city_data['population_mil'].idxmax()] # idxmax() returns index of max value
print("\nCity with largest population:\n", city_with_max_pop)

city_max_danso = city_data.sort_values(by='density_per_sq_km', ascending=False).iloc[0]
print("\nCity with highest density:\n", city_max_danso)

total_population = city_data['population_mil'].sum()
print("\nTotal population (million):", total_population)

total_area_sq_km = city_data['area_sq_km'].mean()
print("Average area (sq km):", total_area_sq_km)

city_describe = city_data.describe()
print("\nCity DataFrame description:\n", city_describe)

sort_area_sq_km_increasing = city_data.sort_values(by='area_sq_km', ascending=True)
print("\nCity DataFrame sorted by area (increasing):\n", sort_area_sq_km_increasing)

rank_population = city_data['population_mil'].rank(ascending=False)
city_data["population_rank"] = rank_population
print("\nPopulation rank:\n", city_data)