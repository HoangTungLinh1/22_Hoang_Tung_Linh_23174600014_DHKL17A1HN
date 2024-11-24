import pandas as pd

ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])

vi_tri = ser1[ser1.isin(ser2)].index.tolist()

print(vi_tri)
