# Customer Churn Prediction System

## Project Overview

This project predicts whether a telecom customer is likely to leave (churn) using Machine Learning.

The system performs complete data preprocessing, model training, evaluation, and provides predictions through a FastAPI REST API.

---

## Features

- Data Cleaning
- Missing Value Handling
- Feature Encoding
- Logistic Regression Model
- Model Evaluation/
- FastAPI Prediction API

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Joblib

---

## Machine Learning Workflow

1. Load Dataset
2. Exploratory Data Analysis (EDA)
3. Handle Missing Values
4. Remove Unnecessary Columns
5. Encode Categorical Features
6. Train-Test Split
7. Train Logistic Regression
8. Evaluate Model
9. Save Model
10. Build FastAPI API

---

## Model Performance

- Accuracy: **82%**

Metrics Used:

- Accuracy
- Confusion Matrix
- Classification Report

---

## Run Locally

Install dependencies

```bash
pip install -r requirements.txt
```

Run the API

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

## Project Structure

```
Customer-Churn-Prediction/
│
├── app/
│   └── main.py
│
├── data/
│   ├── Telco-Customer-Churn.csv
│   └── cleaned_customer_churn.csv
│
├── models/
│   └── customer_churn_predictor.pkl
│
├── notebook/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Future Improvements

- Random Forest
- XGBoost
- Hyperparameter Tuning
- Docker Deployment
- Streamlit Dashboard
