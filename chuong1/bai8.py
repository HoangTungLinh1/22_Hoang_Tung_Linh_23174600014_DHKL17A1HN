class Date:
    def __init__(self, ngay=1, thang=1, nam=2000):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def display(self):
        print(f"{self.ngay:02d}/{self.thang:02d}/{self.nam}")

    def next(self):
        ngay_trong_thang = [31, 29 if self.la_nam_nhuan() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.ngay += 1

        if self.ngay > ngay_trong_thang[self.thang - 1]:
            self.ngay = 1
            self.thang += 1

            if self.thang > 12:
                self.thang = 1
                self.nam += 1

    def la_nam_nhuan(self):
        return (self.nam % 4 == 0 and self.nam % 100 != 0) or (self.nam % 400 == 0)


class Employee:
    def __init__(self, ten, ngay_sinh, ngay_vao):
        self.ten = ten
        self.ngay_sinh = ngay_sinh
        self.ngay_vao = ngay_vao

    def display(self):
        print(f"Tên: {self.ten}")
        print("Ngày sinh: ", end="")
        self.ngay_sinh.display()
        print("Ngày vào công ty: ", end="")
        self.ngay_vao.display()


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for employee in self.employees:
            employee.display()
            print("")

manager = EmployeeManager()

emp1 = Employee("Thu", Date(15, 5, 1990), Date(1, 1, 2020))
emp2 = Employee("Hoang", Date(20, 10, 1992), Date(15, 3, 2021))

manager.add_employee(emp1)
manager.add_employee(emp2)

manager.display_employees()
