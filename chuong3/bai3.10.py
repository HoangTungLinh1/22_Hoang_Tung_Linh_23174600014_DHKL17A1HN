import csv
import numpy as np

filename = 'chuong3/drinks.csv'
with open(filename, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  
    data = [row for row in reader]  

countries = [row[0] for row in data]
beer_servings = np.array([int(row[1]) for row in data if row[1]])
spirit_servings = np.array([int(row[2]) for row in data if row[2]])
wine_servings = np.array([int(row[3]) for row in data if row[3]])
total_alcohol = np.array([float(row[4]) for row in data if row[4]])
continents = [row[5] for row in data]

print("Dữ liệu các cột:", header)
print("Kích thước dữ liệu:", len(data))

continent_beer = {}
for i, continent in enumerate(continents):
    if continent not in continent_beer:
        continent_beer[continent] = []
    continent_beer[continent].append(beer_servings[i])

print("\nSố lượng bia tiêu thụ trung bình ở mỗi châu lục:")
for continent, servings in continent_beer.items():
    print(f"{continent}: {np.mean(servings)}")

continent_wine = {}
for i, continent in enumerate(continents):
    if continent not in continent_wine:
        continent_wine[continent] = []
    continent_wine[continent].append(wine_servings[i])

print("\nThông tin thống kê tổng quát về rượu vang:")
for continent, servings in continent_wine.items():
    print(f"{continent}: {np.mean(servings):.2f} trung bình, {np.min(servings)} thấp nhất, {np.max(servings)} cao nhất")

print("\nSố lượng bia và rượu tiêu thụ trung bình ở mỗi châu lục:")
for continent in continent_beer:
    print(f"{continent}: Bia - {np.mean(continent_beer[continent]):.2f}, Rượu - {np.mean(continent_wine.get(continent, [0])):.2f}")

print("\nGiá trị trung vị bia và rượu tiêu thụ:")
for continent in continent_beer:
    print(f"{continent}: Bia - {np.median(continent_beer[continent]):.2f}, Rượu - {np.median(continent_wine.get(continent, [0])):.2f}")

continent_spirit = {}
for i, continent in enumerate(continents):
    if continent not in continent_spirit:
        continent_spirit[continent] = []
    continent_spirit[continent].append(spirit_servings[i])

print("\nSố lượng rượu mạnh tiêu thụ:")
for continent, servings in continent_spirit.items():
    print(f"{continent}: Trung bình - {np.mean(servings):.2f}, Lớn nhất - {np.max(servings)}, Nhỏ nhất - {np.min(servings)}")

sorted_beer = sorted(zip(countries, beer_servings), key=lambda x: x[1])

print("\n5 quốc gia tiêu thụ bia nhiều nhất:")
for country, beer in sorted_beer[-5:]:
    print(f"{country}: {beer}")

print("\n5 quốc gia tiêu thụ bia ít nhất:")
for country, beer in sorted_beer[:5]:
    print(f"{country}: {beer}")
