
import streamlit as st
import pandas as pd

# Load the hotel features data
try:
    hotel_features = pd.read_csv("hotel_features.csv")
except FileNotFoundError:
    st.error("hotel_features.csv not found. Please ensure the file is in the same directory.")
    st.stop()

st.title('Hotel Recommendation Engine')
st.write('Find hotels based on your preferred city, price range, and length of stay.')

# Get unique places for the selectbox
places = hotel_features['place'].unique().tolist()

# Input widgets
selected_city = st.selectbox('Destination City', places)
min_price = st.slider('Minimum Nightly Price ($)', min_value=0.0, max_value=500.0, value=50.0, step=1.0)
max_price = st.slider('Maximum Nightly Price ($)', min_value=0.0, max_value=500.0, value=300.0, step=1.0)
min_days = st.slider('Minimum Days of Stay', min_value=1, max_value=10, value=1, step=1)
max_days = st.slider('Maximum Days of Stay', min_value=1, max_value=10, value=5, step=1)

if st.button('Suggest Hotels'):
    # Filter the dataset by destination
    matches = hotel_features[hotel_features['place'] == selected_city]

    # Narrow down based on nightly rate
    within_budget = matches[(matches['hotel_price'] >= min_price) & (matches['hotel_price'] <= max_price)]

    # Final filter for the number of days
    final_selection = within_budget[within_budget['days'].between(min_days, max_days)]

    if not final_selection.empty:
        st.subheader(f'Recommended Hotels in {selected_city}:')
        st.dataframe(final_selection.reset_index(drop=True))
    else:
        st.info('No hotels found matching your criteria. Try adjusting your selections.')
