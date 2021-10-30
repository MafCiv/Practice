import pandas as pd
import os

df = pd.read_cvs("./titanic-2.csv")
df.head(5)
print(df.PassengerId)