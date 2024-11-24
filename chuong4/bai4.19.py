import pandas as pd
import numpy as np

fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))

print("Quả:", fruit.tolist())
print("Trọng lượng:", weights.tolist())

khoi_luong_TB = weights.groupby(fruit).mean()
print("Khối lượng trung bình:")
print(khoi_luong_TB)
