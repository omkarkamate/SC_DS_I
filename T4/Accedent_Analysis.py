import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# LOAD DATA
# ---------------------------
data = pd.read_csv("Accedent.csv")

cols = [
    "HOUR", "DAY_WEEK", "MONTH",
    "WEATHERNAME", "LGT_CONDNAME",
    "MAX_SEVNAME", "NUM_INJ"
]

data = data[cols]

data = data.dropna()

data = data[(data["HOUR"] >= 0) & (data["HOUR"] <= 23)]


print(data.head())
print(data.info())

plt.figure(figsize=(10,5))
sns.countplot(x="HOUR", data=data)
plt.title("Accidents by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x="DAY_WEEK", data=data)
plt.title("Accidents by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Accidents")
plt.show()

plt.figure(figsize=(10,6))
data["WEATHERNAME"].value_counts().head(10).plot(kind="bar")
plt.title("Top Weather Conditions for Accidents")
plt.xlabel("Weather Condition")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(y="LGT_CONDNAME", data=data)
plt.title("Accidents by Light Condition")
plt.xlabel("Count")
plt.ylabel("Light Condition")
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x="MAX_SEVNAME", data=data)
plt.title("Accident Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(data["NUM_INJ"], bins=20)
plt.title("Injury Distribution")
plt.xlabel("Number of Injuries")
plt.ylabel("Frequency")
plt.show()

print("\nKey Insights:")
print("- Most accidents occur during peak hours.")
print("- Weather conditions significantly impact accidents.")
print("- Poor lighting conditions increase accident occurrence.")
print("- Majority accidents have moderate severity.")