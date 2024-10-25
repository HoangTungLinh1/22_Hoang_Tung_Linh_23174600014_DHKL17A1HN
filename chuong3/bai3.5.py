import numpy as np

with open('chuong3/heights_1.txt', 'r') as f:
    height = [float(line.strip()) for line in f if line.strip()]

with open('chuong3/weights_1.txt', 'r') as f:
    weight = [float(line.strip()) for line in f if line.strip()]

arr_height = np.array(height)
arr_weight = np.array(weight)

arr_height_m = arr_height * 0.0254

arr_weight_kg = arr_weight * 0.453592

arr_bmi = arr_weight_kg / (arr_height_m ** 2)

if len(arr_weight_kg) > 50:
    weight_at_index_50 = arr_weight_kg[50]
    print("Cân nặng tại vị trí index 50:", weight_at_index_50)
else:
    print("Không có cân nặng tại vị trí index 50, kích thước mảng nhỏ hơn 50.")

if len(arr_height_m) > 110:
    arr_height_m_100 = arr_height_m[100:111]
    print("Chiều cao từ index 100 đến 110:", arr_height_m_100)
else:
    print("Không có chiều cao từ index 100 đến 110, mảng không đủ lớn.")

players_bmi_less_21 = arr_bmi[arr_bmi < 21]
print("Cầu thủ có BMI < 21:", players_bmi_less_21)

mean_height = np.mean(arr_height_m)
mean_weight = np.mean(arr_weight_kg)
print("Chiều cao trung bình:", mean_height)
print("Cân nặng trung bình:", mean_weight)

max_height = np.max(arr_height_m)
max_weight = np.max(arr_weight_kg)
print("Chiều cao lớn nhất:", max_height)
print("Cân nặng lớn nhất:", max_weight)

min_height = np.min(arr_height_m)
min_weight = np.min(arr_weight_kg)
print("Chiều cao nhỏ nhất:", min_height)
print("Cân nặng nhỏ nhất:", min_weight)