# Task 03: Decision Tree Classifier

## Objective

To build a machine learning model that predicts whether a customer will subscribe to a term deposit using the Bank Marketing dataset.

---

## Dataset

The dataset contains customer information such as:

* Age
* Job
* Marital Status
* Education
* Housing Loan
* Personal Loan

Target variable:

* **y** → Whether the customer subscribed (Yes/No)

---

## Steps Performed

### 1. Data Loading

* Loaded dataset using Pandas
* Selected relevant features for analysis

### 2. Data Preprocessing

* Removed rows with unknown values
* Encoded categorical variables using Label Encoding
* Scaled numerical feature (age)

### 3. Train-Test Split

* Split dataset into training (80%) and testing (20%)

### 4. Handling Imbalanced Data

* Applied **SMOTE (Synthetic Minority Oversampling Technique)**
* Balanced the dataset to improve model performance

### 5. Model Building

* Used **Decision Tree Classifier**
* Trained model on resampled training data

### 6. Model Evaluation

* Calculated accuracy
* Generated confusion matrix

---

## Tools Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn (SMOTE)

---

## Results

* **Accuracy:** ~78.5%

### Confusion Matrix:

```
[[5820 1037]
 [ 612  219]]
```

---

## Key Insights

* The model performs well in predicting the majority class (customers who did not subscribe)
* It struggles to accurately predict the minority class (customers who subscribed)
* Even after applying SMOTE, some imbalance effects remain
* Decision Tree provides a simple and interpretable model for classification

---

## Conclusion

This task demonstrates how machine learning models can be used for classification problems.
The Decision Tree model achieved reasonable accuracy, but further improvements can be made by:

* Using advanced models (Random Forest, Gradient Boosting)
* Improving feature selection
* Hyperparameter tuning

---

## Future Improvements

* Apply GridSearch for hyperparameter tuning
* Try ensemble models like Random Forest
* Improve recall for minority class
* Perform feature importance analysis

---
