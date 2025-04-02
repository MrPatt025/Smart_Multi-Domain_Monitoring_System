# filepath: app.py
from flask import Flask, jsonify, request
from modules.data_acquisition import connect_mqtt
from modules.anomaly_detection import AnomalyDetector
from modules.real_time_processing import process_data
import asyncio

# Initialize Flask app
app = Flask(__name__)

# Initialize global variables
detector = AnomalyDetector()
mqtt_client = None

@app.route('/')
def home():
    return jsonify({"message": "Smart Multi-Domain Monitoring System is running!"})

@app.route('/train', methods=['POST'])
def train_model():
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({"error": "No training data provided"}), 400
        detector.train(data)
        return jsonify({"message": "Model trained successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        predictions = detector.predict(data)
        return jsonify({"predictions": predictions.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def start_mqtt():
    global mqtt_client
    mqtt_client = connect_mqtt(broker="localhost", port=1883, topic="sensor/data")

def start_async_processing():
    asyncio.run(process_data())

if __name__ == '__main__':
    # Start MQTT client
    start_mqtt()
    # Start async processing in a separate thread
    asyncio.get_event_loop().run_in_executor(None, start_async_processing)
    # Run Flask app
    app.run(debug=True)

