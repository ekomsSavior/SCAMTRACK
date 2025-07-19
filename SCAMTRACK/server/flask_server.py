# server/flask_server.py
from flask import Flask, request, jsonify, send_from_directory
from server.webhook_reporter import send_to_discord
from server.payload_handler import save_data
import os

app = Flask(__name__)
LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')

@app.route('/')
def index():
    return "SCAMTRACK Flask Server is running!"

@app.route('/tracker/<payload_type>', methods=['POST'])
def tracker(payload_type):
    data = request.get_json(force=True)
    print(f"[+] Received {payload_type} data: {data}")
    save_data(payload_type, data)
    send_to_discord(payload_type, data)
    return jsonify({"status": "received", "payload_type": payload_type})

@app.route('/payloads/<filename>')
def serve_payload(filename):
    return send_from_directory('../payloads', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
