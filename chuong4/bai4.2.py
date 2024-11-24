import numpy as np
import pandas as pd

mylist= list('abcedfghijklmnopqrstuvwxyz')
myarr=np.arange(26)
mydict=dict(zip(mylist, myarr))
ser = pd.Series(mydict)

df = pd.DataFrame({'chu cai': ser.index, 'gia tri': ser.values})
print(df)
