from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('loan_predictor_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:        
        user_data = request.get_json()
        user_df = pd.DataFrame([user_data])  
        prediction = model.predict(user_df)
        result = {'loan_outcome': int(prediction[0])} 
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
