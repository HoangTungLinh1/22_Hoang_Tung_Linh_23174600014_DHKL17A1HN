import numpy as np
import pandas as pd

np.random.seed(100)
ser = pd.Series(np.random.randint(1, 5, 12))

value_counts = ser.value_counts()

top_2 = value_counts.nlargest(2).index

ser.loc[~ser.isin(top_2)] = 'Other'

print(ser)