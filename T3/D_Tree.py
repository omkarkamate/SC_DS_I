import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df=pd.read_csv("bank.csv")
df=df[[]]

print(df.columns)