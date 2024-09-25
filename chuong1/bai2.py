class ThiSinh:
    def __init__(self):
        self.ho_ten = ""
        self.diem_toan = 0.0
        self.diem_ly = 0.0
        self.diem_hoa = 0.0

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def in_thong_tin(self):
        tong_diem = self.tinh_tong_diem()
        print(f"Họ tên thí sinh: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}")
        print(f"Điểm Lý: {self.diem_ly}")
        print(f"Điểm Hóa: {self.diem_hoa}")
        print(f"Tổng điểm: {tong_diem}")

def nhap_danh_sach_thi_sinh(so_thi_sinh):
    danh_sach = []
    for i in range(so_thi_sinh):
        print(f"\nNhập thông tin cho thí sinh thứ {i + 1}:")
        ts = ThiSinh()
        ts.nhap_thong_tin()
        danh_sach.append(ts)
    return danh_sach

def in_danh_sach_trung_tuyen(danh_sach, diem_chuan):
    thi_sinh_trung_tuyen = [ts for ts in danh_sach if ts.tinh_tong_diem() >= diem_chuan]
    thi_sinh_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)
    if thi_sinh_trung_tuyen:
        print("\nDanh sách thí sinh trúng tuyển:")
        for ts in thi_sinh_trung_tuyen:
            ts.in_thong_tin()
    else:
        print("\nKhông có thí sinh nào trúng tuyển.")

DIEM_CHUAN = 20


so_thi_sinh = int(input("Nhập số lượng thí sinh: "))
danh_sach_thi_sinh = nhap_danh_sach_thi_sinh(so_thi_sinh)
in_danh_sach_trung_tuyen(danh_sach_thi_sinh, DIEM_CHUAN)

