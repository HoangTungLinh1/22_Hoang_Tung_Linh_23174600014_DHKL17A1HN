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
        if (self.nam % 4 == 0 and self.nam % 100 != 0) or (self.nam % 400 == 0):
            return True
        return False

date = Date(28, 2, 2024)
date.display()  
date.next()     
date.display()  
date.next()     
date.display() 
