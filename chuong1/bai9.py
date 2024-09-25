import math
class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh

    def chu_vi(self):
        raise NotImplementedError("Các lớp con phải triển khai phương thức này")

    def dien_tich(self):
        raise NotImplementedError("Các lớp con phải triển khai phương thức này")

class HinhBinhHanh(DaGiac):
    def __init__(self, day, cao):
        super().__init__(4)  
        self.day = day
        self.cao = cao

    def chu_vi(self):
        return 2 * (self.day + self.cao)

    def dien_tich(self):
        return self.day * self.cao

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, dai, rong):
        super().__init__(rong, dai)  

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)  

print("1. Hình bình hành")
day = float(input("Nhập chiều dài đáy: "))
cao = float(input("Nhập chiều cao: "))
hinh_binh_hanh = HinhBinhHanh(day, cao)
print(f"Chu vi hình bình hành: {hinh_binh_hanh.chu_vi()}")
print(f"Diện tích hình bình hành: {hinh_binh_hanh.dien_tich()}")

print("\n2. Hình chữ nhật")
dai = float(input("Nhập chiều dài: "))
rong = float(input("Nhập chiều rộng: "))
hinh_chu_nhat = HinhChuNhat(dai, rong)
print(f"Chu vi hình chữ nhật: {hinh_chu_nhat.chu_vi()}")
print(f"Diện tích hình chữ nhật: {hinh_chu_nhat.dien_tich()}")

print("\n3. Hình vuông")
canh = float(input("Nhập chiều dài cạnh: "))
hinh_vuong = HinhVuong(canh)
print(f"Chu vi hình vuông: {hinh_vuong.chu_vi()}")
print(f"Diện tích hình vuông: {hinh_vuong.dien_tich()}")
