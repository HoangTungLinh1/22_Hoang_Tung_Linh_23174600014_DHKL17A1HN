import numpy as np

heights = []
positions = []

with open('chuong3/heights_1.txt', 'r') as f:
    for line in f:
        heights.append(float(line.strip()))

with open('chuong3/position.txt', 'r') as f:
    for line in f:
        positions.append(line.strip())

np_positions = np.array(positions)
print("Kiểu dữ liệu của np_positions:", np_positions.dtype)

np_heights = np.array(heights)
print("Kiểu dữ liệu của np_heights:", np_heights.dtype)

gk_heights = np_heights[np_positions == 'GK']
average_height_gk = np.mean(gk_heights)
print("\nChiều cao trung bình của các GK:", average_height_gk)

non_gk_heights = np_heights[np_positions != 'GK']
average_height_non_gk = np.mean(non_gk_heights)
print("Chiều cao trung bình của những vị trí khác:", average_height_non_gk)

players_dtype = np.dtype([('position', 'U5'), ('height', 'float')])
players = np.zeros(len(positions), dtype=players_dtype)

players['position'] = np_positions
players['height'] = np_heights

sorted_players = np.sort(players, order='height')

highest_player = sorted_players[-1]
lowest_player = sorted_players[0]

print("\nVị trí cầu thủ cao nhất:", highest_player['position'], "với chiều cao:", highest_player['height'])
print("Vị trí cầu thủ thấp nhất:", lowest_player['position'], "với chiều cao:", lowest_player['height'])
