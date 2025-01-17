import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter
''' 
1) ignore the missing data... or remove them
2) averaging the data...  most frequet value .. median ...
'''

dataset = pd.read_csv('Data.csv')
# df = pd.DataFrame(dataset)
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan,strate gy='mean')
# fit method will find and replace it..
imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])
print(X)

from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import OneHotEncoder

