import pandas as pd
#df = pd.read_csv("data.csv")
df = pd.read_csv(r"C:\Users\shuma\Desktop\Data\data.csv")
Q1 = df["UnitPrice"].quantile(0.25)
Q3 = df["UnitPrice"].quantile(0.75)
IQR = Q3 - Q1

outlier_rows = df[(df["UnitPrice"] < Q1 - 1.5*IQR) | (df["UnitPrice"] > Q3 + 1.5*IQR)]
print(outlier_rows)