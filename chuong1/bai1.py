class HinhChuNhat:
    def __init__(self):
        self.dai = 0
        self.rong = 0

    def nhap_du_lieu(self):
        self.dai = float(input("Nhập chiều dài của hình chữ nhật: "))
        self.rong = float(input("Nhập chiều rộng của hình chữ nhật: "))

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def in_thong_tin(self):
        chu_vi = self.tinh_chu_vi()
        dien_tich = self.tinh_dien_tich()
        print(f"Chiều dài: {self.dai}")
        print(f"Chiều rộng: {self.rong}")
        print(f"Chu vi: {chu_vi}")
        print(f"Diện tích: {dien_tich}")


hcn = HinhChuNhat()
hcn.nhap_du_lieu()
hcn.in_thong_tin()
