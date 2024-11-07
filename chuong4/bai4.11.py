import pandas as pd

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

ket_qua = ser.iloc[pos]

print(ser)

print(ket_qua)
