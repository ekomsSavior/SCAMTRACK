#!/usr/bin/env python3

import subprocess
import time
import os
import json
import socket
from pathlib import Path
import qrcode
import random
import requests
import shutil

PAYLOADS_DIR = "payloads"
OBF_DIR = os.path.join(PAYLOADS_DIR, "obf_payloads")
SCAM_QR_DIR = "scam_qr"
CHAINED_FILENAME = "chained_payload.html"

os.makedirs(PAYLOADS_DIR, exist_ok=True)
os.makedirs(OBF_DIR, exist_ok=True)
os.makedirs(SCAM_QR_DIR, exist_ok=True)

def is_flask_up(host="127.0.0.1", port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        return sock.connect_ex((host, port)) == 0

def launch_flask_server():
    print(" Launching Flask trap server...")
    subprocess.Popen(["python3", "-m", "server.flask_server"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(10):
        if is_flask_up():
            print(" Flask server is up and listening on port 5000.")
            return
        time.sleep(1)
    print(" Flask server failed to start.")
    exit(1)

def launch_ngrok():
    print(" Starting Ngrok tunnel on port 5000...")
    subprocess.Popen(["ngrok", "http", "5000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5)
    try:
        res = subprocess.check_output(["curl", "-s", "http://localhost:4040/api/tunnels"])
        tunnels = json.loads(res)["tunnels"]
        public_url = tunnels[0]["public_url"]
        print(f" Ngrok Public URL: {public_url}\n")
        return public_url
    except Exception as e:
        print(f"[!] Ngrok error: {e}")
        return None

def list_payloads():
    return sorted([f for f in os.listdir(PAYLOADS_DIR) if f.endswith(".html") or f.endswith(".js")])

def obfuscate_filename(original_filename):
    names = [
        "invoice_2025.html", "login_error.html", "google_auth_update.html",
        "session_timeout.html", "email_verify_2fa.html", "mfa_reset.html"
    ]
    return random.choice(names)

def shorten_url(long_url):
    try:
        print(" 🔧 Shortening URL via is.gd...")
        res = requests.get("https://is.gd/create.php", params={"format": "simple", "url": long_url})
        if res.status_code == 200:
            short = res.text.strip()
            print(f" Shortened: {short}")
            return short
    except:
        print(" Failed to shorten URL.")
    return long_url

def upload_custom_payload():
    path = input(" Path to your payload (.html or .js): ").strip()
    if not os.path.isfile(path):
        print(" File not found.")
        return
    dest = os.path.join(PAYLOADS_DIR, os.path.basename(path))
    subprocess.run(["cp", path, dest])
    print(f" Payload saved as: {dest}")

def generate_qr(link, filename_hint="qr_code"):
    qr_path = os.path.join(SCAM_QR_DIR, f"{filename_hint}_qr.png")
    img = qrcode.make(link)
    img.save(qr_path)
    print(f" Saved QR code to: {qr_path}")

def build_chained_payload(selected_payloads):
    full_paths = [os.path.join(PAYLOADS_DIR, list_payloads()[i]) for i in selected_payloads]
    lines = []
    for f in full_paths:
        if f.endswith(".html"):
            lines.append(f'<iframe src="{os.path.basename(f)}" style="display:none;"></iframe>')
        elif f.endswith(".js"):
            lines.append(f'<script src="{os.path.basename(f)}"></script>')
    chained = "\n".join(lines)
    with open(os.path.join(PAYLOADS_DIR, CHAINED_FILENAME), "w") as out:
        out.write(chained)
    print(f" Created {CHAINED_FILENAME} from:")
    for i in selected_payloads:
        print(f"  - {list_payloads()[i]}")
    return CHAINED_FILENAME

def trap_payload_picker(public_url):
    print(" Available Payloads:")
    payloads = list_payloads()
    for i, p in enumerate(payloads, 1):
        print(f"[{i}] {p}")
    print(f"[{len(payloads)+1}] Chain Multiple Payloads")

    choice = input("Select a payload: ").strip()
    if not choice.isdigit():
        print(" Invalid selection.")
        return
    choice = int(choice)

    if choice == len(payloads)+1:
        indices = input(" Choose payloads to chain (comma-separated): ").strip().split(",")
        try:
            selected_indices = [int(i)-1 for i in indices if i.strip().isdigit()]
            filename = build_chained_payload(selected_indices)
        except:
            print(" Invalid selection.")
            return
    elif 1 <= choice <= len(payloads):
        filename = payloads[choice-1]
    else:
        print(" Invalid selection.")
        return

    original_path = os.path.join(PAYLOADS_DIR, filename)
    obf_name = obfuscate_filename(filename)
    obf_path = os.path.join(OBF_DIR, obf_name)
    shutil.copyfile(original_path, obf_path)

    full_link = f"{public_url}/payloads/obf_payloads/{obf_name}"
    short_link = shorten_url(full_link)

    print(f"\n Your trap link is cloaked:\n{short_link}\n")

    q = input("[?] Generate QR code for this link? (y/n): ").lower()
    if q == "y":
        generate_qr(short_link, Path(obf_name).stem)

def main_menu():
    while True:
        print("""
 ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▄ ▄▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▄▄▄▄   ▄▀▀▄ █ 
█ █   ▐ █ █    ▌ ▐ ▄▀ ▀▄ █  █ ▀  █ █    █  ▐ █   █   █ ▐ ▄▀ ▀▄ █ █    ▌ █  █ ▄▀ 
   ▀▄   ▐ █        █▄▄▄█ ▐  █    █ ▐   █     ▐  █▀▀█▀    █▄▄▄█ ▐ █      ▐  █▀▄  
▀▄   █    █       ▄▀   █   █    █     █       ▄▀    █   ▄▀   █   █        █   █ 
 █▀▀▀    ▄▀▄▄▄▄▀ █   ▄▀  ▄▀   ▄▀    ▄▀       █     █   █   ▄▀   ▄▀▄▄▄▄▀ ▄▀   █  
 ▐      █     ▐  ▐   ▐   █    █    █         ▐     ▐   ▐   ▐   █     ▐  █    ▐  
        ▐                ▐    ▐    ▐                           ▐        ▐       
            by ekomsSavi0r
""")
        print("""
[1] Build Full Trap (Flask + Ngrok + Payload Picker)
[2] Upload Your Own Payload
[3] View Live Logs
[4] Recon a Suspicious Scam Domain
[5] Exit
""")
        choice = input("Select option: ").strip()

        if choice == "1":
            launch_flask_server()
            url = launch_ngrok()
            if url:
                trap_payload_picker(url)
        elif choice == "2":
            upload_custom_payload()
        elif choice == "3":
            print(" Press Ctrl+C to return to menu.")
            subprocess.call(["tail", "-f", "logs/tracker_events.log"])
        elif choice == "4":
            domain = input(" 🔎 Enter domain to scan: ").strip()
            subprocess.call(["python3", "scam_domain_tracker.py", domain])
        elif choice == "5":
            print(" Exiting ScamTrack. Stay safe out there.")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
