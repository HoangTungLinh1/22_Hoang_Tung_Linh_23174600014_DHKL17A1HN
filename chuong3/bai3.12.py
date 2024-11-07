import numpy as np

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            row = line.strip().split(',')
            data.append(row)
    return np.array(data)

movies = read_csv('chuong3/movies.csv')
ratings = read_csv('chuong3/ratings.csv')
tags = read_csv('chuong3/tags.csv')
links = read_csv('chuong3/links.csv')

print("Movies Data:")
print("Shape:", movies.shape)
print("Columns:", movies[0])  
print("Sample data (first 5 rows):")
print(movies[1:6])  

print("\nRatings Data:")
print("Shape:", ratings.shape)
print("Columns:", ratings[0])
print("Sample data (first 5 rows):")
print(ratings[1:6])

print("\nTags Data:")
print("Shape:", tags.shape)
print("Columns:", tags[0])
print("Sample data (first 5 rows):")
print(tags[1:6])

print("\nLinks Data:")
print("Shape:", links.shape)
print("Columns:", links[0])
print("Sample data (first 5 rows):")
print(links[1:6])

ratings_cleaned = ratings.copy()
ratings_cleaned[ratings_cleaned == ''] = '0'

movie_ids = ratings_cleaned[1:, 1].astype(int)
movie_titles = movies[1:, 0]  

combined_data = []
for rating in ratings_cleaned[1:]:
    movie_id = int(rating[1])
    if movie_id < len(movie_titles):
        title = movie_titles[movie_id]
        combined_data.append([title, rating[2]])  

combined_array = np.array(combined_data)
print("\nCombined Data (Movie Title and Ratings):")
print(combined_array[:5])  

ratings_float = ratings_cleaned[1:, 2].astype(float)
average_ratings = {}
for i, title in enumerate(movie_titles):
    if title in average_ratings:
        average_ratings[title].append(ratings_float[i])
    else:
        average_ratings[title] = [ratings_float[i]]

average_ratings = {title: np.mean(rating) for title, rating in average_ratings.items()}
high_rated_movies = {title: rating for title, rating in average_ratings.items() if rating >= 4}

print("\nHigh Rated Movies (Average Rating >= 4):")
for title, rating in high_rated_movies.items():
    print(f"{title}: {rating}")

total_movies = len(movie_titles)
print("\nTotal number of movies:", total_movies)

timestamps = ratings[1:, 0].astype(int) 
dates = np.array([np.datetime64(ts, 's') for ts in timestamps])

print("\nParsed Dates from Ratings:")
print(dates[:5])  

print("\nAll operations completed.")
