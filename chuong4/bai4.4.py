import numpy as np
import pandas as pd

ser1= pd.Series([1,2,3,4,5])
ser2= pd.Series([4,5,6,7,8])

set1 = set(ser1)
set2 = set(ser2)

print("co o ser1 ma khong o ser2", set1.difference(ser2))

print("co o ser1 va ser2 nhung khong nam chung ca hai", set1.symmetric_difference(ser2))