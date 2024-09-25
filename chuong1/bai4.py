class Stack:
    def __init__(self, kich_thuoc_toi_da):
        self.stack = [] 
        self.kich_thuoc_toi_da = kich_thuoc_toi_da 

    def __del__(self):
        del self.stack 

    def push(self, gia_tri):
        if not self.isFull():
            self.stack.append(gia_tri)
            print(f"Đã thêm {gia_tri} vào ngăn xếp.")
        else:
            print("Ngăn xếp đã đầy, không thể thêm phần tử.")

    def pop(self):
        if not self.isEmpty():
            gia_tri = self.stack.pop()
            print(f"Đã lấy {gia_tri} ra khỏi ngăn xếp.")
            return gia_tri
        else:
            print("Ngăn xếp trống, không thể lấy phần tử.")
            return None

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.kich_thuoc_toi_da

    def print_stack(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Nội dung ngăn xếp:", self.stack)

stack = Stack(5)
    
stack.push(1.5)
stack.push(2.3)
stack.push(4.7)
stack.push(3.6)
stack.push(5.2)
    
stack.push(4.2)
    
stack.print_stack()
    
stack.pop()
stack.pop()
    
stack.print_stack()
    
if stack.isEmpty():
    print("Ngăn xếp trống.")
else:
    print("Ngăn xếp không trống.")
