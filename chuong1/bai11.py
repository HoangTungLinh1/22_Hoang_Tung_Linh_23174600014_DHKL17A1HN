import math
class TamGiac:
    def __init__(self, a, b, c):
        self.a = a  
        self.b = b  
        self.c = c  

    def chu_vi(self):
        return self.a + self.b + self.c

    def dien_tich(self):
        p = self.chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def display(self):
        print(f"Các cạnh của tam giác: a = {self.a}, b = {self.b}, c = {self.c}")
        print(f"Chu vi: {self.chu_vi()}")
        print(f"Diện tích: {self.dien_tich()}")

class TamGiacCan(TamGiac):
    def __init__(self, canh, day):
        super().__init__(canh, canh, day)  

class TamGiacVuong(TamGiac):
    def __init__(self, canh_a, canh_b):
        canh_c = math.sqrt(canh_a**2 + canh_b**2)
        super().__init__(canh_a, canh_b, canh_c)

    def display(self):
        super().display()
        print("Đây là tam giác vuông.")

class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh)  

    def display(self):
        super().display()
        print("Đây là tam giác đều.")

print("Nhập thông tin cho tam giác:")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
tam_giac = TamGiac(a, b, c)
tam_giac.display()

print("\nNhập thông tin cho tam giác vuông:")
canh_a = float(input("Nhập cạnh a: "))
canh_b = float(input("Nhập cạnh b: "))
tam_giac_vuong = TamGiacVuong(canh_a, canh_b)
tam_giac_vuong.display()

print("\nNhập thông tin cho tam giác cân:")
canh = float(input("Nhập cạnh bằng nhau: "))
day = float(input("Nhập cạnh đáy: "))
tam_giac_can = TamGiacCan(canh, day)
tam_giac_can.display()

print("\nNhập thông tin cho tam giác đều:")
canh_deu = float(input("Nhập chiều dài cạnh: "))
tam_giac_deu = TamGiacDeu(canh_deu)
tam_giac_deu.display()
