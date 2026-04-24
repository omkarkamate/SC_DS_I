# Task 04: Traffic Accident Data Analysis

## Objective

To analyze real-world traffic accident data and identify patterns based on time, weather conditions, lighting, and accident severity.

---

## Dataset

US Traffic Accidents Dataset (2020)

The dataset contains detailed records of road accidents including:

* Time of accident (Hour, Day, Month)
* Weather conditions
* Light conditions
* Accident severity
* Number of injuries

---

## Features Used

For this analysis, only relevant columns were selected:

* **HOUR** – Hour of accident
* **DAY_WEEK** – Day of week
* **MONTH** – Month of accident
* **WEATHERNAME** – Weather condition
* **LGT_CONDNAME** – Light condition
* **MAX_SEVNAME** – Severity of accident
* **NUM_INJ** – Number of injuries

---

## Steps Performed

### 1. Data Loading

* Loaded dataset using Pandas

### 2. Data Cleaning

* Selected necessary columns
* Removed missing values
* Filtered valid hour values (0–23)

### 3. Exploratory Data Analysis (EDA)

* Analyzed accident distribution based on:

  * Hour of the day
  * Day of the week
  * Weather conditions
  * Light conditions
  * Severity levels

### 4. Data Visualization

* Created multiple plots using Matplotlib and Seaborn:

  * Accidents by hour
  * Accidents by day
  * Weather condition impact
  * Light condition analysis
  * Severity distribution
  * Injury distribution

---

## Tools Used

* Python
* Pandas
* Matplotlib
* Seaborn

---

## Key Insights

* Most accidents occur during peak traffic hours
* Weather conditions significantly influence accident frequency
* Poor lighting conditions (night/dark) increase accident occurrence
* Majority of accidents fall under moderate severity levels
* Most accidents involve a low number of injuries

---

## Conclusion

This analysis highlights important patterns in traffic accidents.
Understanding these factors can help in improving road safety, traffic management, and preventive measures.

---

## Future Improvements

* Perform location-based accident analysis
* Use machine learning to predict accident severity
* Analyze trends across multiple years
* Build an interactive dashboard using Power BI or Tableau

---
