import numpy as np

# 1. Đọc dữ liệu từ file heights_1.txt và weights_1.txt
with open('chuong3/heights_1.txt', 'r') as f:
    height = [float(line.strip()) for line in f if line.strip()]

with open('chuong3/weights_1.txt', 'r') as f:
    weight = [float(line.strip()) for line in f if line.strip()]

# 2. Tạo numpy array từ danh sách height và weight
arr_height = np.array(height)
arr_weight = np.array(weight)

# 3. Chuyển đổi chiều cao từ inch sang mét (1 inch = 0.0254 m)
arr_height_m = arr_height * 0.0254

# 4. Chuyển đổi cân nặng từ pounds sang kg (1 pound = 0.453592 kg)
arr_weight_kg = arr_weight * 0.453592

# 5. Tính BMI (BMI = weight (kg) / (height (m)^2))
arr_bmi = arr_weight_kg / (arr_height_m ** 2)

# 6. Lấy cân nặng ở vị trí index 50 trong arr_weight_kg (kiểm tra kích thước mảng trước)
if len(arr_weight_kg) > 50:
    weight_at_index_50 = arr_weight_kg[50]
    print("Cân nặng tại vị trí index 50:", weight_at_index_50)
else:
    print("Không có cân nặng tại vị trí index 50, kích thước mảng nhỏ hơn 50.")

# 7. Lấy chiều cao từ index 100 đến 110 trong arr_height_m (nếu mảng đủ lớn)
if len(arr_height_m) > 110:
    arr_height_m_100 = arr_height_m[100:111]
    print("Chiều cao từ index 100 đến 110:", arr_height_m_100)
else:
    print("Không có chiều cao từ index 100 đến 110, mảng không đủ lớn.")

# 8. Tìm các cầu thủ có BMI < 21
players_bmi_less_21 = arr_bmi[arr_bmi < 21]
print("Cầu thủ có BMI < 21:", players_bmi_less_21)

# 9. Tính chiều cao và cân nặng trung bình
mean_height = np.mean(arr_height_m)
mean_weight = np.mean(arr_weight_kg)
print("Chiều cao trung bình:", mean_height)
print("Cân nặng trung bình:", mean_weight)

# 10. Tìm chiều cao và cân nặng lớn nhất
max_height = np.max(arr_height_m)
max_weight = np.max(arr_weight_kg)
print("Chiều cao lớn nhất:", max_height)
print("Cân nặng lớn nhất:", max_weight)

# 11. Tìm chiều cao và cân nặng nhỏ nhất
min_height = np.min(arr_height_m)
min_weight = np.min(arr_weight_kg)
print("Chiều cao nhỏ nhất:", min_height)
print("Cân nặng nhỏ nhất:", min_weight)