
from flask import Flask, jsonify
from model import get_predictions

app = Flask(__name__)

@app.route('/api/ping')
def ping():
    return jsonify({'message': 'W0LFICR backend is alive'})

@app.route('/api/predict')
def predict():
    prediction = get_predictions()
    return jsonify({'prediction': prediction})
