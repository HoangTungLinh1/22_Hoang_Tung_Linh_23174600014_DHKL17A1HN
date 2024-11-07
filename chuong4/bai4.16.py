import pandas as pd

ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])

hieu_so=ser.iloc[1:].reset_index(drop=True) - ser.iloc[:-1].reset_index(drop=True)

print(hieu_so)