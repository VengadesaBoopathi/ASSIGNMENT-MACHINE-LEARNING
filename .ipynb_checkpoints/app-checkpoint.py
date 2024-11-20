from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model (this should be done once at the start)
model = joblib.load('loan_predictor_model.pkl')

# Endpoint to get the prediction for a user
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the user data from the request
        user_data = request.get_json()

        # Ensure the user data is in the correct format (e.g., a dictionary)
        user_df = pd.DataFrame([user_data])  # Convert the input JSON into a DataFrame

        # Apply any necessary preprocessing (such as feature engineering, encoding, etc.)
        # Example: if the model uses features like age ranges or logarithmic transformations, 
        # make sure the necessary preprocessing is applied here

        # Make the prediction using the model
        prediction = model.predict(user_df)

        # Return the prediction result
        return jsonify({'loan_outcome': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
