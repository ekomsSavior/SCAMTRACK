# scamtrack_launcher.py

import os
import time
import subprocess
import requests
import socket

def banner():
    print(r"""
 ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▄ ▄▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▄▄▄▄   ▄▀▀▄ █ 
█ █   ▐ █ █    ▌ ▐ ▄▀ ▀▄ █  █ ▀  █ █    █  ▐ █   █   █ ▐ ▄▀ ▀▄ █ █    ▌ █  █ ▄▀ 
   ▀▄   ▐ █        █▄▄▄█ ▐  █    █ ▐   █     ▐  █▀▀█▀    █▄▄▄█ ▐ █      ▐  █▀▄  
▀▄   █    █       ▄▀   █   █    █     █       ▄▀    █   ▄▀   █   █        █   █ 
 █▀▀▀    ▄▀▄▄▄▄▀ █   ▄▀  ▄▀   ▄▀    ▄▀       █     █   █   ▄▀   ▄▀▄▄▄▄▀ ▄▀   █  
 ▐      █     ▐  ▐   ▐   █    █    █         ▐     ▐   ▐   ▐   █     ▐  █    ▐  
        ▐                ▐    ▐    ▐                           ▐        ▐       
        by ekomsSavi0r
    """)

def is_port_open(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        return result == 0

def launch_ngrok():
    print("🚀 Launching Ngrok tunnel on port 5000...")

    subprocess.Popen(["/usr/local/bin/ngrok", "http", "5000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("⏳ Waiting for Ngrok to initialize...", end="", flush=True)

    for _ in range(20):
        if is_port_open("localhost", 4040):
            print(" ✅")
            break
        time.sleep(1)
        print(".", end="", flush=True)
    else:
        print("\n❌ Ngrok API never became available. Make sure the authtoken is set:")
        print("   ngrok config add-authtoken <your_token>")
        return

    try:
        res = requests.get("http://localhost:4040/api/tunnels")
        tunnels = res.json().get("tunnels", [])
        if tunnels:
            public_url = tunnels[0]["public_url"]
            print(f"\n🌐 Ngrok Public URL: {public_url}")
        else:
            print("❌ No active tunnels found.")
    except Exception as e:
        print(f"\n❌ Failed to connect to Ngrok API: {e}")

def main():
    banner()
    print("[1] Start Flask Trap Server")
    print("[2] Launch Ngrok Tunnel")
    print("[3] View Live Logs")
    print("[4] Open Payloads Folder")
    print("[5] Generate QR Code from Payload Link")
    print("[6] Recon a Suspicious Scam Domain")
    print("[7] Exit\n")

    choice = input("Select option: ")

    if choice == "1":
        os.system("python3 -m server.flask_server")
    elif choice == "2":
        launch_ngrok()
    elif choice == "3":
        os.system("python3 view_logs.py")
    elif choice == "4":
        os.system("xdg-open payloads")
    elif choice == "5":
        os.system("python3 qr_generator.py")
    elif choice == "6":
        os.system("python3 scam_domain_tracker.py")
    elif choice == "7":
        print("Bye 👋")
        exit()
    else:
        print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
