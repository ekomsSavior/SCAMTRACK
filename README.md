# SCAMTRACK

track and trace with SCAMTRACK

![IMG_7347](https://github.com/user-attachments/assets/33d3999d-c5e5-4824-be73-bcc5ffd7de41)


**SCAMTRACK** offers a modular suite of payloads, trackers, recon tools, and logging mechanisms to ethically investigate scam activity, teach anti-phishing concepts, and help defenders stay ahead.

use SCAMTRACK in conjuction with PHISH HUNTER PRO https://github.com/ekomsSavior/PHISH_HUNTER_PRO for maximum scammer carnage xo

---

##  FEATURES

-  Flask trap server for logging recon data from scammer clicks
-  Payloads to gather IPs, device info, screenshots, clipboard content, and more
-  Ngrok tunneling for public access to traps
-  QR Code trap generator for physical or mobile lures
-  Domain recon engine to investigate phishing links
-  Live log viewer for terminal-based real-time output
-  CLI launcher for noob-friendly access to all tools
-  Dynamic trap builder with optional redirect support
-  Optional Discord webhook alerts
-  100% open-source, modular, and designed for defenders

---

##  INSTALLATION

###  Requirements

- Python 3.10+  
- Kali Linux or any Linux distro  
- Ngrok (Free or Personal Plan)

```bash
pip install -r requirements.txt
```
to get the proper flask version you may need to run:

```bash
pip install -r requirements.txt --break-system-packages
```

---

##  USAGE

### 1. Clone the repo

```bash
git clone https://github.com/ekomsSavior/SCAMTRACK.git
cd SCAMTRACK
```
### Install and Set Up Ngrok

```bash
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
rm ngrok-stable-linux-amd64.zip
chmod +x ngrok
```
###
Then authenticate Ngrok:

```bash
ngrok config add-authtoken $YOUR_AUTHTOKEn
```

### 2. CLI Launcher Mode (All-in-One Interface)

Run:

```bash
python3 scamtrack_launcher.py
```

From here, you can:

* Launch Flask server
* Start Ngrok
* Tail logs
* Generate payloads or QR codes
* Do recon

>  NOTE: The CLI interface **does not run Flask + Ngrok in the background** yet.
> You’ll still need to open **multiple terminals** if you want Flask, Ngrok, and SCAMTRACK tools running *at the same time*. This will be streamlined in a future version.
---

##  CLI OPTIONS

| Option               | Description                           |
| -------------------- | ------------------------------------- |
| Start Flask Server   | Launches the local trap server        |
| Launch Ngrok         | Opens a public tunnel to port 5000    |
| View Logs            | See trap results live in the terminal |
| Open Payloads Folder | View/edit trap payloads               |
| Generate QR Code     | Converts payload links to QR traps    |
| Recon a Scam Domain  | Investigate suspicious URLs           |
| Exit                 | Close the tool                        |

---

##  INCLUDED PAYLOADS

| Payload                   | Description                                          |
| ------------------------- | ---------------------------------------------------- |
| `ip_grabber.html`         | Logs IP, headers, timezone, screen, UA               |
| `clipboard_stealer.js`    | Attempts to read clipboard content                   |
| `device_fingerprint.html` | Collects OS, fonts, screen, battery                  |
| `screenshot_captor.html`  | Uses html2canvas to capture browser viewport         |
| `bait_redirect.html`      | Logs info, then redirects to a real login page       |
| `deep_recon.html`         | Silently loads scam infra via iframes                |
| `app_launcher.html`       | Tests URI scheme launches (intent://, tel:, etc.)    |
| `*_trap.html`             | Auto-generated custom payloads with redirect support |

---

##  UTILITIES

| File                     | Purpose                                           |
| ------------------------ | ------------------------------------------------- |
| `qr_generator.py`        | Generates QR codes from any payload URL           |
| `payload_generator.py`   | CLI tool to build payloads with optional redirect |
| `scam_domain_tracker.py` | Investigates scam domains using WHOIS, IP, GeoIP  |
| `view_logs.py`           | Tails the trap logs live in your terminal         |
| `logs/`                  | JSON + TXT logs from all payload hits             |

---

##  HOW TO DEPLOY A TRAP - Manual Mode (Advanced Users)

###  1. Start the trap server

```bash
python3 -m server.flask_server
```

Server will run on `http://localhost:5000`.

---

###  2. Start Ngrok in a seperate terminal: 

```bash
ngrok http 5000
```

Ngrok will give you a public URL like:

```
https://abc123.ngrok.app → http://localhost:5000
```

This is your **trap base URL**.

---

###  3. Send a payload link

Example:

```
https://abc123.ngrok.app/payloads/ip_grabber.html
```

---

##  HOW TO BUILD A CUSTOM TRAP 

```bash
python3 payload_generator.py
```

* Input a payload name (e.g., `ip`, `phishbait`)
* Input an optional redirect (e.g., `https://paypal.com`)
* Result: `payloads/phishbait_trap.html`

---

##  HOW TO MAKE A QR CODE 

```bash
python3 qr_generator.py
```

* Paste your Ngrok payload URL
* Output: `payloads/scamtrack_qr.png`

---

## LOGGING OPTIONS

*  Local logs (JSON + text in `/logs/`)
*  Live terminal view: `python3 view_logs.py`
*  Optional: Set a Discord webhook (in `server/webhook_reporter.py`)

---

## ETHICAL DISCLAIMER

**SCAMTRACK is for ethical research only use on systems and networks you have permission to test on.

---

Thank you for you friendship and continued support homies. sending hugs always.
### xox _ek0mssavi0r

---

![IMG_7347](https://github.com/user-attachments/assets/33d3999d-c5e5-4824-be73-bcc5ffd7de41)


