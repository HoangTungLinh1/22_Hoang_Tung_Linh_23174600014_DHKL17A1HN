import numpy as np
import pandas as pd

ser = pd.Series(np.random.randint(1, 10, 35))
#np.random.randint tao mang gom 35 so nguyen ngau nhien tu 1 den 9
#pd.Series chuyen doi mang du lieu thanh pandas

print(pd.DataFrame(ser.values.reshape(7, 5)))