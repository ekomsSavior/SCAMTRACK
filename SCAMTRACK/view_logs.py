import os
import time

LOG_PATH = "logs/tracker_events.log"

def ensure_log_file():
    os.makedirs("logs", exist_ok=True)
    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w") as f:
            f.write("SCAMTRACK log initialized. Waiting for events...\n")

def tail(filepath):
    with open(filepath, 'r') as f:
        f.seek(0, 2)  # Move to EOF
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            print(line.strip())

if __name__ == "__main__":
    print("📺 Live View - tracker_events.log\n")
    ensure_log_file()
    try:
        tail(LOG_PATH)
    except KeyboardInterrupt:
        print("\n💤 Exiting live view.")
