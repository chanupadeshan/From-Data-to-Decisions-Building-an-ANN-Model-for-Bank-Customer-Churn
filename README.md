# Customer Churn Prediction Web App

This project is a Flask-based web application for predicting whether a customer will leave a bank (churn) based on their details. The prediction is made using a pre-trained deep learning model built in TensorFlow/Keras.

## 📄 Features

- Web interface for customer input
- One-hot encoding for geographical data
- Model prediction using saved .h5 model and scaler
- Easy integration and modification

## ⚙️ Technologies Used

- Python
- Flask
- TensorFlow / Keras
- Scikit-learn
- HTML (Jinja2 templating)

## 📁 Project Structure

```
.
├── app.py                  # Flask app
├── model/
│   ├── model.h5           # Trained Keras model
│   └── scaler.pkl         # Fitted Scikit-learn scaler
├── templates/
│   └── index.html         # UI form for user input
├── Churn_Modelling.csv    # Dataset (for reference/training)
└── Churn_Modelling.ipynb  # Jupyter notebook for model training
```

## ⚡ Quick Start

1. Clone the repository

   ```bash
   git clone <repo_url>
   cd <project_folder>
   ```

2. Install dependencies


   ```bash
   pip install flask tensorflow scikit-learn
   ```

3. Run the Flask app

   ```bash
   python app.py
   ```

   App will be running at [http://127.0.0.1:5001](http://127.0.0.1:5001)

## 📊 Input Features

- Geography: France, Germany, Spain
- Credit Score
- Gender: Male or Female
- Age
- Tenure: Years with the bank
- Balance
- Number of Products
- Has Credit Card: Yes/No
- Is Active Member: Yes/No
- Estimated Salary

## 🔬 Model Details

- Trained on the Churn_Modelling.csv dataset
- Input features normalized using scaler.pkl
- Binary classification output:
  - 0 = Will stay
  - 1 = Will leave

## 🚀 Example

**Input sample:**

- Geography: France
- Credit Score: 600
- Gender: Female
- Age: 40
- Tenure: 3
- Balance: 60000
- Number of Products: 2
- Credit Card: Yes
- Active Member: No
- Estimated Salary: 50000

**Output:** The customer will stay with the bank 