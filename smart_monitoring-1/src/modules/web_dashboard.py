from flask import Blueprint, jsonify, request
from flask_cors import CORS

web_dashboard = Blueprint('web_dashboard', __name__)
CORS(web_dashboard)

@web_dashboard.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    # Validate and process the incoming data
    # Add your data processing logic here
    return jsonify({"status": "success", "message": "Data received"}), 200

@web_dashboard.route('/', methods=['GET'])
def index():
    # Render the main dashboard page
    return jsonify({"message": "Welcome to the Smart Multi-Domain Monitoring System Dashboard"}), 200

def create_app():
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(web_dashboard, url_prefix='/dashboard')
    return app