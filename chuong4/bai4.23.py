import pandas as pd

ratings = pd.read_csv('chuong4/ratings.csv')  

print("Data Types:")
print(ratings.dtypes)
print("\nData Shape:")
print(ratings.shape)
print("\nColumns:")
print(ratings.columns)

print("\nDataset Info:")
print(ratings.info())

missing_values = ratings.isnull().sum()
print("\nMissing Values:")
print(missing_values)

if missing_values.sum() > 0:
    print("\nFilling missing values with the median:")
    ratings = ratings.fillna(ratings.median())  
    print(ratings.isnull().sum())  

print("\nDescriptive Statistics:")
print(ratings.describe())

invalid_ratings = ratings[(ratings['rating'] < 0.5) | (ratings['rating'] > 5)]
print("\nInvalid Ratings:")
print(invalid_ratings)

if not invalid_ratings.empty:
    print("\nRemoving invalid ratings...")
    ratings = ratings[(ratings['rating'] >= 0.5) & (ratings['rating'] <= 5)]
    print("\nRemaining dataset:")
    print(ratings)

print("\nFirst 5 rows of the dataset:")
print(ratings.head())
