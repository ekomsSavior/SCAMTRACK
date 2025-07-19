# scamtrack_launcher.py

import os
import time
import subprocess
import requests

def banner():
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
        print("🚀 Launching Ngrok tunnel on port 5000...")
        try:
            subprocess.Popen(["./ngrok", "http", "5000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(6)

            try:
                res = requests.get("http://localhost:4040/api/tunnels")
                tunnels = res.json().get("tunnels", [])
                if tunnels:
                    public_url = tunnels[0]["public_url"]
                    print(f"\n🌐 Ngrok Public URL: {public_url}")
                else:
                    print("❌ Ngrok tunnel not found.")
            except requests.exceptions.RequestException as e:
                print(f"\n❌ Failed to connect to Ngrok API: {e}")

        except Exception as e:
            print(f"\n❌ Failed to launch Ngrok: {e}")

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
