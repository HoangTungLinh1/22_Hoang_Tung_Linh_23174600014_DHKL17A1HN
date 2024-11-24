import pandas as pd

drinks = pd.read_csv('chuong4\drinks.csv', index_col=0)

print("Data Type:")
print(drinks.dtypes)
print("\nData Shape:")
print(drinks.shape)
print("\nColumns:")
print(drinks.columns)

print("\nFirst 5 rows:")
print(drinks.head())
print("\nLast 5 rows:")
print(drinks.tail())

print("\nAverage alcohol consumption per continent:")
print(drinks.groupby('continent').mean())

print("\nDescriptive statistics per continent:")
print(drinks.groupby('continent').describe())

print("\nMean beer servings per continent:")
print(drinks.groupby('continent')['beer_servings'].mean())
print("\nMean total alcohol consumption per continent:")
print(drinks.groupby('continent')['total_litres_of_pure_alcohol'].mean())

print("\nMedian beer servings per continent:")
print(drinks.groupby('continent')['beer_servings'].median())
print("\nMedian total alcohol consumption per continent:")
print(drinks.groupby('continent')['total_litres_of_pure_alcohol'].median())

print("\nSpirit servings statistics per continent:")
print(drinks.groupby('continent')['spirit_servings'].agg(['mean', 'max', 'min']))

sorted_drinks = drinks.sort_values(by='beer_servings')
print("\nData sorted by beer servings:")
print(sorted_drinks)

min_beer_continent = drinks.groupby('continent')['beer_servings'].sum().idxmin()
max_beer_continent = drinks.groupby('continent')['beer_servings'].sum().idxmax()
print(f"\nContinent with minimum beer consumption: {min_beer_continent}")
print(f"Continent with maximum beer consumption: {max_beer_continent}")
