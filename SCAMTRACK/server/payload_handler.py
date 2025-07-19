# server/payload_handler.py
import json
import os
from datetime import datetime

LOG_PATH = os.path.join(os.path.dirname(__file__), '..', 'logs', 'captured_data.json')
EVENT_LOG = os.path.join(os.path.dirname(__file__), '..', 'logs', 'tracker_events.log')

def save_data(payload_type, data):
    timestamp = datetime.utcnow().isoformat()
    entry = {
        "timestamp": timestamp,
        "payload_type": payload_type,
        "data": data
    }

    try:
        # Try loading existing JSON
        if os.path.exists(LOG_PATH):
            try:
                with open(LOG_PATH, 'r') as f:
                    current = json.load(f)
            except json.JSONDecodeError:
                print("[!] JSON decode failed. Resetting captured_data.json")
                current = []
        else:
            current = []

        # Append new entry
        current.append(entry)
        with open(LOG_PATH, 'w') as f:
            json.dump(current, f, indent=2)

        # Append to raw log
        with open(EVENT_LOG, 'a') as f:
            f.write(f"[{timestamp}] {payload_type.upper()} - {data}\n")

    except Exception as e:
        print(f"[!] Error saving data: {e}")
