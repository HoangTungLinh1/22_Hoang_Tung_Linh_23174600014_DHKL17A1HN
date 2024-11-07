import numpy as np
import pandas as pd

ser1= pd.Series(list("abcedfghijklmnopqrstuvwxyz"))
ser2= pd.Series(np.arange(26))

print(pd.DataFrame({'chu cai': ser1, "so": ser2}))