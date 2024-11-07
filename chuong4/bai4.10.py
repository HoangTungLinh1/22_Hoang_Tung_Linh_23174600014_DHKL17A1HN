import numpy as np
import pandas as pd

ser = pd.Series(np.random.randint(1, 10, 7))

print(ser)

vi_tri_boi_cua_3 = [i for i in range(len(ser)) if ser.iloc[i] % 3 == 0]

print(vi_tri_boi_cua_3)
