import streamlit as st
import requests
from datetime import datetime

st.title("Wacon Cab")
# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride
# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''
# Date and time input
date_time = st.date_input('Date', datetime.now())
time = st.time_input('Time', datetime.now().time())
pickup_datetime = datetime.combine(date_time, time)
# Pickup and dropoff location inputs
pickup_longitude = st.number_input('Pickup Longitude', value=0.0)
pickup_latitude = st.number_input('Pickup Latitude', value=0.0)
dropoff_longitude = st.number_input('Dropoff Longitude', value=0.0)
dropoff_latitude = st.number_input('Dropoff Latitude', value=0.0)
# Passenger count input
passenger_count = st.number_input('Passenger Count', min_value=1, max_value=8, value=1)
# '''
# ## Once we have these, let's call our API in order to retrieve a prediction
# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...
# :thinking_face: How could we call our API ? Off course... The `requests` package :bulb:
# '''
url = 'https://taxifare.lewagon.ai/predict'
# if url == 'https://taxifare.lewagon.ai/predict':
#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
# '''
# 2. Let's build a dictionary containing the parameters for our API...
# 3. Let's call our API using the `requests` package...
# 4. Let's retrieve the prediction from the **JSON** returned by the API...
# ## Finally, we can display the prediction to the user
# '''
# Build the parameters dictionary
params = {
    'pickup_datetime': pickup_datetime.strftime('%Y-%m-%d %H:%M:%S'),
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}
# Call the API and get the prediction
if st.button('Get Fare Prediction'):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        prediction = response.json().get('fare', 'Error: No fare returned')
        st.write(f'Estimated Fare: ${prediction}')
    else:
        st.write('Error: Failed to retrieve prediction')


import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Replace 'your_api_url' with your prediction API URL
    url = 'https://your_api_url/predict'
    # Collect data from form or API call
    data = request.get_json(force=True)
    # Send data to prediction API
    response = requests.post(url, json=data)
    prediction = response.json()

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
