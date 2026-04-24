import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder,StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.metrics import confusion_matrix

df = pd.read_csv("bank.csv", sep=";")
df.columns = df.columns.str.strip()
df = df[["age","job","marital","education","housing","loan","y"]]

# print(df.head())

SScaler=StandardScaler()
df["age"]=SScaler.fit_transform(df[["age"]])

for col in ["marital","education","housing","loan"]:
    df=df[df[col]!="unknown"]


LEncoder=LabelEncoder()
for col in ["job","marital","education","housing","loan","y"]:
    df[col]=LEncoder.fit_transform(df[col])

X=df.drop("y",axis=1)
y=df["y"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train_res, y_train_res) 
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy:.4f}")
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
