import numpy as np
import pandas as pd

ser = pd.Series(np.random.normal(10, 5, 25))

min = ser.min()
percentile_25 = ser.quantile(0.25)
Trung_vi = ser.median()
percentile_75 = ser.quantile(0.75)
maX = ser.max()

print("Minimum value of ser:", min)
print("25th percentile of ser:", percentile_25)
print("Median of ser:", Trung_vi)
print("75th percentile of ser:", percentile_75)
print("Maximum value of ser:", max)
