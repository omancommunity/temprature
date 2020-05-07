import pandas as pd
import numpy as np


df = pd.read_csv('salalah.csv', usecols=[
    "Date(TL) (2)","Salalah Temp.Dry Avg [deg C] (2)"
])

print(df.describe())
print(df)

# print(df['Date(TL) (2)'])



