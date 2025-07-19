# utils/generate_ngrok_url.py
import requests
import subprocess
import time

def launch_ngrok(port=5000):
    print("🚀 Launching Ngrok tunnel on port 5000...")
    subprocess.Popen(["./ngrok", "http", str(port)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)

    try:
        res = requests.get("http://localhost:4040/api/tunnels")
        tunnels = res.json().get("tunnels", [])
        if tunnels:
            return tunnels[0]["public_url"]
        else:
            print("❌ Ngrok tunnel not found. Is ngrok running?")
            return None
    except Exception as e:
        print(f"❌ Failed to get Ngrok URL: {e}")
        return None
