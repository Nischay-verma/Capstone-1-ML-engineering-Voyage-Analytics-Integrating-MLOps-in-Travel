
import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model and encoders
try:
    flight_rf = joblib.load('flight_price_model_rf.joblib')
    le_from = joblib.load('le_from.joblib')
    le_to = joblib.load('le_to.joblib')
    le_flightType = joblib.load('le_flightType.joblib')
    le_agency = joblib.load('le_agency.joblib')
    print("Model and encoders loaded successfully.")
except Exception as e:
    print(f"Error loading model or encoders: {e}")
    exit()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)

        # Extract features from the request data
        input_data = {
            'from': data['from'],
            'to': data['to'],
            'flightType': data['flightType'],
            'agency': data['agency'],
            'time': float(data['time']),
            'distance': float(data['distance'])
        }

        # Encode categorical features
        encoded_from = le_from.transform([input_data['from']])[0]
        encoded_to = le_to.transform([input_data['to']])[0]
        encoded_flight_type = le_flightType.transform([input_data['flightType']])[0]
        encoded_agency = le_agency.transform([input_data['agency']])[0]

        # Create input DataFrame for prediction
        features = pd.DataFrame([[
            encoded_from,
            encoded_to,
            encoded_flight_type,
            encoded_agency,
            input_data['time'],
            input_data['distance']
        ]], columns=['from_num', 'to_num', 'flightType_num', 'agency_num', 'time', 'distance'])

        # Make prediction
        prediction = flight_rf.predict(features)[0]

        return jsonify({'predicted_price': round(float(prediction), 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
