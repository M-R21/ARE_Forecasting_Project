from flask import Flask, request, jsonify
from src.models.evaluate_model import evaluate_model

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Logic to predict ARE cases
    return jsonify({'prediction': 'value'})

if __name__ == '__main__':
    app.run(debug=True)
