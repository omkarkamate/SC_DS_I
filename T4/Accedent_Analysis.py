import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("acc_20.csv")

# ---------------------------
# BASIC INFO
# ---------------------------
print(data.head())
print(data.info())

# ---------------------------
# CLEANING
# ---------------------------
# Remove missing values
data = data.dropna()

# ---------------------------
# ANALYSIS
# ---------------------------

# Accidents by Hour
sns.countplot(x='HOUR', data=data)
plt.title("Accidents by Hour")
plt.show()

# Accidents by Weather
sns.countplot(x='WEATHER', data=data)
plt.title("Accidents by Weather")
plt.xticks(rotation=45)
plt.show()

# Accidents by Day of Week
sns.countplot(x='DAY_WEEK', data=data)
plt.title("Accidents by Day")
plt.show()

# Accident Severity
sns.countplot(x='SEVERITY', data=data)
plt.title("Accident Severity Distribution")
plt.show()