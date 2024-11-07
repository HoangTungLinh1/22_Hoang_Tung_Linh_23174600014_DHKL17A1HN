import pandas as pd
import numpy as np

truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)

sai_so = ((truth - pred) ** 2).mean()

print("sai so binh phuong trung binh:", sai_so)