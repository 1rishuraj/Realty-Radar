# Run this in pycharm Local via server directory : python server.py
# Check only at the mentioned paths like http://localhost:5000/predict_home_price
# Now run live server in html while server.py is running in pycharm
from flask import Flask, request, jsonify
import util

app = Flask(__name__)

# app.route defines the endpoint eg. '/get_location_names' and the request method
@app.route('/get_location_names', methods=['GET']) 
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    # request.form is same as request.body
    # request.form['key_name'] here 'key_name' correspond to $.post( keys variable names passed )
    total_sqft = float(request.form['total_sqft']) 
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    # common practice or syntax
    response.headers.add('Access-Control-Allow-Origin', '*')
    # returns the estimated price from modrl prediction fxn in util 
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run() # runs application at specific port