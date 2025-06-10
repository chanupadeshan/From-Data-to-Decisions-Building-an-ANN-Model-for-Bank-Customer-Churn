from flask import Flask, render_template, request
import tensorflow as tf

import pickle

def onehotencoding(Geography):
    """One-hot encode the Geography feature."""
    country = ['France', 'Germany', 'Spain']
    encoded_list = [1 if item == Geography else 0 for item in country]
    return encoded_list



def prediction(list):
    model = tf.keras.models.load_model("model\model.h5")
    with open ('model\scaler.pkl','rb') as f:
        sc = pickle.load(f)
        
    transformed_list = sc.transform([list])
    pred_probability = model.predict(transformed_list)
    
    pred = 1 if pred_probability > 0.5 else 0
    return pred


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Render the form."""
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    """Process form data and return predictions."""
    
    # Get form values
    Geography = request.form['Geography']
    Credit_score = int(request.form['Credit_score'])
    Gender = 1 if request.form['Gender'] == 'Male' else 0
    Age = int(request.form['Age'])
    Tenure = int(request.form['Tenure'])
    Balance = float(request.form['Balance'])
    products = int(request.form['Num_of_products'])
    Credit_card = 1 if request.form['Credit_card'] == 'Yes' else 0
    Active_member = 1 if request.form['Active_member'] == 'Yes' else 0
    Salary = float(request.form['Estimated_salary'])
    # Create a fresh feature list
    feature_list = onehotencoding(Geography) + [Credit_score, Gender, Age, Tenure, Balance,products, Credit_card, Active_member,Salary]
    
    print(feature_list)  # Debugging output

    # Get the prediction
    pred = prediction(feature_list)
    if pred == 1:
        predicted_text = 'The customer will leave the bank'
    else:
        predicted_text = 'The customer will stay with the bank'
    
    
    return render_template('index.html', predicted_text = predicted_text , prediction = pred)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
