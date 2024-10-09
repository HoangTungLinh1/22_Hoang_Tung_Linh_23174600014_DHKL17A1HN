import json

def luu_giao_dich(cac_giao_dich):
    ten_file = "giao_dich.json"
    with open(ten_file, 'w', encoding='utf-8') as f:
        json.dump(cac_giao_dich, f, ensure_ascii=False, indent=4)
    print(f"Danh sách giao dịch đã được ghi vào file {ten_file}")

def thuc_hien_giao_dich():
    cac_giao_dich = {"giao_dich_tien": []}
    
    while True:
        print("Thực hiện giao dịch tiền")
        so_luong = float(input("Nhập số tiền giao dịch: "))
        giao_dich = {"loại": "tiền", "số lượng": so_luong}
        cac_giao_dich["giao_dich_tien"].append(giao_dich)
        
        them_giao_dich = input("Bạn có muốn thực hiện thêm giao dịch? (1: Có, 0: Không): ")
        if them_giao_dich == "0":
            break
    
    return cac_giao_dich

cac_giao_dich = thuc_hien_giao_dich()
    
lua_chon = input("Bạn có muốn ghi danh sách giao dịch vào tệp không? (1: Có, 0: Không): ")
    
if lua_chon == "1":
    luu_giao_dich(cac_giao_dich)
else:
    print("Danh sách giao dịch không được ghi vào file.")
