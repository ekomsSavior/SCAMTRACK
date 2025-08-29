import json
import os
from datetime import datetime

LOG_PATH = os.path.join(os.path.dirname(__file__), '..', 'logs', 'captured_data.json')
EVENT_LOG = os.path.join(os.path.dirname(__file__), '..', 'logs', 'tracker_events.log')
LOOT_DIR = os.path.join(os.path.dirname(__file__), '..', 'loot')
os.makedirs(LOOT_DIR, exist_ok=True)

def save_data(payload_type, data):
    timestamp = datetime.utcnow().isoformat()
    entry = {
        "timestamp": timestamp,
        "payload_type": payload_type,
        "data": data
    }

    try:
        # Load or create the main JSON log
        if os.path.exists(LOG_PATH):
            try:
                with open(LOG_PATH, 'r') as f:
                    current = json.load(f)
            except json.JSONDecodeError:
                print("[!] JSON decode failed. Resetting captured_data.json")
                current = []
        else:
            current = []

        current.append(entry)
        with open(LOG_PATH, 'w') as f:
            json.dump(current, f, indent=2)

        # Log raw text
        with open(EVENT_LOG, 'a') as f:
            f.write(f"[{timestamp}] {payload_type.upper()} - {data}\n")

        # Save to separate loot file for Hijax module
        loot_file = os.path.join(LOOT_DIR, f"{payload_type}_{timestamp.replace(':', '-')}.json")
        with open(loot_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"[+] Saved to {loot_file}")

    except Exception as e:
        print(f"[!] Error saving data: {e}")
