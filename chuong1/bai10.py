import math
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Diem: ({self.x}, {self.y})")


class Elip(Diem):
    def __init__(self, x, y, ban_kinh_a, ban_kinh_b):
        super().__init__(x, y)  
        self.ban_kinh_a = ban_kinh_a  
        self.ban_kinh_b = ban_kinh_b  

    def dien_tich(self):
        return math.pi * self.ban_kinh_a * self.ban_kinh_b

    def display(self):
        super().display()  
        print(f"Ban kính a: {self.ban_kinh_a}, Ban kính b: {self.ban_kinh_b}")
        print(f"Diện tích elip: {self.dien_tich()}")


class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh) 

    def display(self):
        super().display()  
        print(f"Diện tích đường tròn: {self.dien_tich()}")

print("Nhập thông tin cho elip:")
x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
ban_kinh_a = float(input("Nhập bán kính trục lớn (a): "))
ban_kinh_b = float(input("Nhập bán kính trục nhỏ (b): "))

elip = Elip(x, y, ban_kinh_a, ban_kinh_b)
elip.display()

print("\nNhập thông tin cho đường tròn:")
ban_kinh = float(input("Nhập bán kính đường tròn: "))
duong_tron = DuongTron(x, y, ban_kinh)
duong_tron.display()
