class PhanSo:
    def __init__(self):
        self.tu_so = 0
        self.mau_so = 1

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        while self.mau_so == 0:
            print("Mẫu số không thể bằng 0. Vui lòng nhập lại!!!")
            self.mau_so = int(input("Nhập mẫu số: "))

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def in_phan_so(self):
        print(f"Phân số: {self.tu_so}/{self.mau_so}")

phan_so = PhanSo()
phan_so.nhap_phan_so()
if phan_so.kiem_tra_hop_le():
    phan_so.in_phan_so()
else:
    print("Phân số không hợp lệ.")
