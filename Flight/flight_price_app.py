
import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model and encoders
try:
    flight_rf = joblib.load('flight_price_model_rf.joblib')
    le_from = joblib.load('le_from.joblib')
    le_to = joblib.load('le_to.joblib')
    le_flightType = joblib.load('le_flightType.joblib')
    le_agency = joblib.load('le_agency.joblib')
except FileNotFoundError:
    st.error("Model or encoder files not found. Please ensure 'flight_price_model_rf.joblib', 'le_from.joblib', 'le_to.joblib', 'le_flightType.joblib', and 'le_agency.joblib' are in the same directory.")
    st.stop()

st.title('Flight Price Prediction')
st.write('Predict the price of a flight based on various features.')

# Input widgets
selected_from = st.selectbox('Departure Airport', le_from.classes_)
selected_to = st.selectbox('Arrival Airport', le_to.classes_)
selected_flight_type = st.selectbox('Flight Type', le_flightType.classes_)
selected_agency = st.selectbox('Agency', le_agency.classes_)
flight_time = st.slider('Flight Time (hours)', min_value=0.5, max_value=5.0, value=1.5, step=0.1)
flight_distance = st.slider('Flight Distance (km)', min_value=100.0, max_value=2000.0, value=500.0, step=10.0)

if st.button('Predict Flight Price'):
    try:
        # Encode categorical features
        encoded_from = le_from.transform([selected_from])[0]
        encoded_to = le_to.transform([selected_to])[0]
        encoded_flight_type = le_flightType.transform([selected_flight_type])[0]
        encoded_agency = le_agency.transform([selected_agency])[0]

        # Create input DataFrame
        input_data = pd.DataFrame([[encoded_from, encoded_to, encoded_flight_type, encoded_agency, flight_time, flight_distance]],
                                    columns=['from_num', 'to_num', 'flightType_num', 'agency_num', 'time', 'distance'])

        # Make prediction
        prediction = flight_rf.predict(input_data)[0]

        st.success(f'Predicted Flight Price: ${prediction:.2f}')
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
