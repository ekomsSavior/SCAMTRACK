# view_logs.py
import time

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
    try:
        tail("logs/tracker_events.log")
    except KeyboardInterrupt:
        print("\n💤 Exiting live view.")

