# Customer Churn Analytics & Prediction

Predicting customer churn using Machine Learning and uncovering the key factors influencing customer retention.

## Project Overview

Customer churn is one of the most important business challenges for subscription-based companies. Retaining existing customers is often more cost-effective than acquiring new ones.

This project analyzes customer behavior patterns and builds machine learning models to predict whether a customer is likely to churn.

The project follows a complete data science workflow:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Training
- Model Evaluation
- Business Insights Generation

---

## Dataset Information

**Dataset:** IBM Telco Customer Churn Dataset

### Dataset Statistics

- Records: 7,032 customers
- Features: 21 columns
- Target Variable: Churn

### Features Include

- Demographics
- Customer tenure
- Contract type
- Internet services
- Payment methods
- Monthly charges
- Total charges

---

## Project Structure

```text
customer-churn-analytics/
│
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   │
│   └── processed/
│       └── cleaned_telco_churn.csv
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_model_training.ipynb
│
├── reports/
│   └── insights.md
│
├── src/
│
├── dashboard/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Exploratory Data Analysis

The dataset was explored to identify patterns and relationships associated with customer churn.

Key analysis areas:

- Churn Distribution
- Contract Type Analysis
- Tenure Analysis
- Monthly Charges Analysis
- Customer Retention Trends

---

## Key Business Insights

### 1. Contract Type Strongly Impacts Churn

Customers on month-to-month contracts exhibit significantly higher churn rates.

### 2. Tenure is a Major Predictor

Customers with shorter tenure are more likely to leave.

### 3. Monthly Charges Influence Churn

Higher monthly charges correlate with increased churn probability.

### 4. Long-Term Customers are More Loyal

Customers with longer relationships tend to remain with the company.

### 5. Most Important Predictors

- Tenure
- Contract Type
- Monthly Charges
- Total Charges

---

## Machine Learning Models

## Model Evaluation

### Random Forest

- Accuracy: 78.82%
- ROC-AUC Score: 0.815
- Precision: 0.63
- Recall: 0.48
- F1 Score: 0.55

The model demonstrates good discriminative capability and effectively identifies customer churn patterns.

### Logistic Regression

Accuracy: **78.54%**

### Random Forest Classifier

Accuracy: **78.82%**

### Model Comparison

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 78.54%   |
| Random Forest       | 78.82%   |

Random Forest achieved the best overall performance.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## Model Deployment

The trained model is saved using Joblib:

```python
import joblib

joblib.dump(model, "models/churn_model.pkl")
```

The model can be loaded for future predictions:

```python
model = joblib.load("models/churn_model.pkl")
```

---

## Future Improvements

- Streamlit Dashboard Deployment
- Hyperparameter Tuning
- ROC-AUC Evaluation
- Precision-Recall Analysis
- XGBoost Implementation
- Real-Time Churn Prediction Interface

---

## Author

Palak Patel

B.Tech ICT Student

Aspiring Data Analyst | Data Science Enthusiast | Machine Learning Learner

```

```
