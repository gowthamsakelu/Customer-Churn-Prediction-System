from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("models/customer_churn_predictor.pkl")


class CustomerData(BaseModel):
    feature: list[float]


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API is Running!"}


@app.post("/predict")
def predict(data: CustomerData):
    prediction = model.predict([data.feature])

    return {
        "Predicted Churn": int(prediction[0])
    }