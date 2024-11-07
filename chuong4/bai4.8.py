import numpy as np
import pandas as pd

ser = pd.Series(np.random.random(20))

phan_vi = np.quantile(ser, np.linspace(0, 1, 11))

ser_copy=ser.copy()

for i in range(10):
    ser_copy.loc[(ser >= phan_vi[i]) & (ser <= phan_vi[i+1])] = f"euqal decile {i+1}"

print(ser_copy)