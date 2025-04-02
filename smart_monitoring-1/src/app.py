from flask import Flask, request, jsonify
from modules.data_acquisition import DataAcquisition
from modules.real_time_processing import RealTimeProcessing
from modules.web_dashboard import WebDashboard

app = Flask(__name__)

# Initialize modules
data_acquisition = DataAcquisition()
real_time_processing = RealTimeProcessing()
web_dashboard = WebDashboard(app)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    real_time_processing.process_data(data)
    return jsonify({"message": "Data received successfully"}), 200

@app.route('/status', methods=['GET'])
def get_status():
    status = real_time_processing.get_status()
    return jsonify(status), 200

@app.route('/', methods=['GET'])
def index():
    return web_dashboard.render_dashboard()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)