
import streamlit as st
import joblib
from sentence_transformers import SentenceTransformer

# Load the trained model and label encoder
try:
    classifier = joblib.load('classifier.pkl')
    label_encoder = joblib.load('label_encoder.pkl')
    # Note: SentenceTransformer model needs to be reloaded as it's not saved via joblib directly
    st_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
except FileNotFoundError:
    st.error("Model or encoder files not found. Please ensure 'classifier.pkl' and 'label_encoder.pkl' are in the same directory.")
    st.stop()

st.title('Gender Classification from Name')
st.write('Enter a first name to predict its likely gender.')

# Input widget
first_name = st.text_input('Enter a first name:')

if st.button('Predict Gender'):
    if first_name:
        try:
            # Generate embedding for the input name
            embedding = st_model.encode([first_name], show_progress_bar=False)

            # Make prediction
            prediction_index = classifier.predict(embedding)[0]
            predicted_gender = label_encoder.inverse_transform([prediction_index])[0]

            st.success(f'Predicted Gender: **{predicted_gender.capitalize()}**')
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
    else:
        st.warning('Please enter a first name.')
