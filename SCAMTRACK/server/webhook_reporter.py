# server/webhook_reporter.py
import requests
import json
import os

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_to_discord(payload_type, data):
    if not WEBHOOK_URL:
        return  # Skip if no webhook set

    embed = {
        "title": f"📡 SCAMTRACK - {payload_type.upper()}",
        "description": f"```json\n{json.dumps(data, indent=2)}```",
        "color": 16711680
    }

    payload = {
        "username": "SCAMTRACK Logger",
        "embeds": [embed]
    }

    try:
        requests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"[!] Failed to send to Discord: {e}")
