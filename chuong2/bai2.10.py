import json

du_lieu={
    "company": {
      "name": "Công ty TNHH Đất Việt",
      "address": "abc Giải Phóng - Hà Nội"
    },
    "employees": {
      "A1": [
        {"name": "Nguyễn Văn A", "age": 25},
        {"name": "Nguyễn Thị B", "age": 24}
      ],
      "A2": [
        {"name": "Trần Thị c", "age": 28},
        {"name": "Trần Thị D", "age": 32},
        {"name": "Trần Thị E", "age": 35}
      ],
      "A3": [
        {"name": "Lê Văn F", "age": 29}
      ],
      "A4": [
          {"name": "Vũ Thị G", "age": 30},
          {"name": "Vũ Thị H", "age": 20}
      ],
      "A5": [
        {"name": "Trịnh Công K", "age": 40}
      ]
    }
}

Tong_NV= sum(len(employees) for employees in du_lieu["employees"].values())

print(f"Tên công ty: {du_lieu['company']['name']}")
print(f"Địa chỉ: {du_lieu['company']['address']}")
print("-----Thống kê nhân viên theo đơn vị-----")

thu_tu=1

for don_vi, employees in du_lieu["employees"].items():
    num_employees = len(employees)
    percentage = (num_employees / Tong_NV) * 100 if Tong_NV > 0 else 0
    print(f"{thu_tu}./Tên đơn vị: Đơn vị {don_vi}.")
    print(f"           - Số nhân viên: {num_employees}")
    print(f"           - Tỷ lệ: {percentage:.2f}%")
    thu_tu += 1

