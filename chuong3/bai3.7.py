import numpy as np

baseball = []
with open('chuong3/baseball.txt', 'r') as f:
    for line in f:
        data = list(map(float, line.strip().split()))
        baseball.append(data)

np_baseball = np.array(baseball)
print("Kiểu dữ liệu của np_baseball:", np_baseball.dtype)
print("Kích thước của np_baseball:", np_baseball.shape)

print("\nGiá trị của dòng thứ 50 trong np_baseball:", np_baseball[49]) 

np_weight = np_baseball[:, 1]
print("\nGiá trị của cột cân nặng (pounds):")
print(np_weight)

height_124 = np_baseball[123, 0]  
print("\nChiều cao của vận động viên thứ 124:", height_124)

tong_height = np.mean(np_baseball[:, 0])
tong_weight = np.mean(np_weight)
print("\nChiều cao trung bình:", tong_height)
print("Cân nặng trung bình:", tong_weight)

su_tuong_quan = np.corrcoef(np_baseball[:, 0], np_weight)[0, 1]
if su_tuong_quan > 0:
    danh_gia_tuong_quan = "có tương quan thuận."
elif su_tuong_quan < 0:
    danh_gia_tuong_quan = "có tương quan nghịch."
else:
    danh_gia_tuong_quan = "không có tương quan."

print(f"\nMối tương quan giữa chiều cao và cân nặng: {danh_gia_tuong_quan} (Hệ số tương quan: {su_tuong_quan:.2f})")
