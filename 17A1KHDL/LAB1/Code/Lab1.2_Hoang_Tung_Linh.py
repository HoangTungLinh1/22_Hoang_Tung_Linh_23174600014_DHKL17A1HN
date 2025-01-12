import json
class JSONReader:
    #Đọc tập Jison
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    def read_json(self):
        with open(self.file_path, 'r') as file:
            self.data = json.load(file)
    #Hiển thị dữ liệu        
    def display_data(self):
        if self.data:
            for user in self.data:
                print(f"Name: {user['name']}, Age: {user['age']}, \Address:{user['address']}")

path = r'D:\python_nang_cao\17A1KHDL\LAB1\DATA\users.json'
reader = JSONReader(path)
reader.read_json()
reader.display_data()
