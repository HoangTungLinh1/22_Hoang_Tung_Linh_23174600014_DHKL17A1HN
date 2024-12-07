import pandas as pd

data = {
    "REGION_ID": [1, 2, 3, 4],
    "REGION_NAME": ["Europe", "Americas", "Asia", "Middle East and Africa"]
}
df = pd.DataFrame(data)
df.to_csv("region.csv", index=False)

df_read = pd.read_csv("region.csv")
print(df_read)
