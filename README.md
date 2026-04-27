# 🚗 Car Price Prediction

A Machine Learning web app that predicts the selling price of used cars based on various features.

## 📊 Dataset
- Source: [Kaggle - Car Price Prediction (Used Cars)](https://www.kaggle.com/datasets/vijayaadithyanvg/car-price-predictionused-cars)
- 301 records with 9 features

## 🧠 Model
- Algorithm: Random Forest Regressor
- R² Score: 0.95
- MAE: 0.63 Lakhs

## 📁 Project Structure
```
├── App.py              # Streamlit web app
├── MyProjects.ipynb    # Jupyter Notebook (EDA + Training)
├── model.pkl           # Trained model
├── encoders.pkl        # Label encoders
├── car data.csv        # Dataset
```

## 🚀 How to Run

1. Install dependencies:
```
pip install streamlit scikit-learn pandas numpy
```

2. Run the app:
```
streamlit run App.py
```

## 🛠️ Features
- Showroom Price
- Kilometers Driven
- Fuel Type (Petrol/Diesel/CNG)
- Transmission (Manual/Automatic)
- Car Age
- Previous Owners
- Seller Type