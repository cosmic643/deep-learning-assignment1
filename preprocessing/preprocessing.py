

import numpy as np
import csv 
import pandas as pd

data = pd.read_csv("data-unprocessed.csv")

data['T_degC'] = data['T_degC'].fillna(data['T_degC'].mean())
data['Salnty'] = data['Salnty'].fillna(data['Salnty'].mean())

data = data[1001:2001]
data.to_csv("final-data-test.csv",index=False)

print(data.head())