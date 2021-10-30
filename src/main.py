import pandas as pd
import os

df = pd.read_tsv("./titanic-2.csv")
df.head(5)
print(df.PassengerId)