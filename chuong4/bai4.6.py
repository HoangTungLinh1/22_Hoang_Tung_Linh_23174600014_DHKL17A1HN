import numpy as np
import pandas as pd

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
#list tao mot danh sach chua cac ky tu tu a den h. 
#np.random.randint tao mang cac so nguyen ngau nhien tu 0 den 7 voi tong cong 30 phan tu
#np.take lay cac phan tu trong list theo cac chi so duoc tao bang np.random.randint.
#pd.Series chuyen ket qua tu np.take thanh pandas

counts = ser.value_counts()

print(counts)