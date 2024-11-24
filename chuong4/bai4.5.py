import numpy as np
import pandas as pd

ser = pd.Series(np.random.normal(10, 5, 25))

min = ser.min()
percentile_25 = ser.quantile(0.25)
Trung_vi = ser.median()
percentile_75 = ser.quantile(0.75)
maX = ser.max()

print("Gia tri min:", min)
print("Phan centile thu 25:", percentile_25)
print("Trung vi:", Trung_vi)
print("phan centile thu 75:", percentile_75)
print("gia tri max:", max)
