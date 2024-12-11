from flask import Flask, render_template, request
import joblib
import numpy as np


app = Flask(__name__)

# Load the models and encoders using joblib
name_encoder = joblib.load('name_encoder.joblib')  # Update path to your actual joblib file
random_forest_model = joblib.load('random_forest_model.joblib')  # Update path to your actual joblib file
target_encoder = joblib.load('target_encoder.joblib')  # Update path to your actual joblib file

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    surname = request.form['surname']
    print(f"Surname received: {surname}")  # Check input

    try:
        # Vectorize the surname using the name_encoder
        # Reshape the input surname to 2D
        surname_vectorized = name_encoder.transform(np.array([surname]).reshape(1, -1))
        print(f"Surname vectorized: {surname_vectorized.shape}")  # Check vectorization

        # Make the prediction using the random forest model
        prediction_encoded = random_forest_model.predict(surname_vectorized)
        print(f"Encoded prediction: {prediction_encoded[0]}")  # Check model output

        # Decode the prediction using the target_encoder
        prediction = target_encoder.inverse_transform([prediction_encoded[0]])[0]
        print(f"Decoded prediction: {prediction}")  # Check final decoded result

        return render_template('result.html', prediction=prediction)
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred while making the prediction.", 500

if __name__ == '__main__':
    app.run(debug=True)
