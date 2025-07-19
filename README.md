# SCAMTRACK

Track and trace with SCAMTRACK  
**by ekomsSavi0r**

![Trap Screenshot](https://github.com/user-attachments/assets/33d3999d-c5e5-4824-be73-bcc5ffd7de41)

SCAMTRACK is a modular phishing trap & scam tracking toolkit.

Pair with [PHISH HUNTER PRO](https://github.com/ekomsSavior/PHISH_HUNTER_PRO) for full-spectrum scammer disruption.

---

##  FEATURES

- Flask trap server to log scammer interactions
- Payloads for IP logging, clipboard, screenshots, device fingerprinting
- Ngrok tunneling for remote trap access
- QR code trap generator
- Scam domain recon engine
- Real-time terminal log viewer
- CLI launcher for noob-friendly access
- Modular, open-source, and 100% designed for defenders

---

##  REQUIREMENTS

- Python 3.10+
- Kali Linux or any Linux distro
- Ngrok (Free or Personal Plan)

---

## INSTALLATION

### 1. Clone the Repo

```bash
git clone https://github.com/ekomsSavior/SCAMTRACK.git
cd SCAMTRACK/SCAMTRACK
````

### 2. Install Dependencies

```bash
sudo apt update && sudo apt install -y python3 python3-pip unzip
pip3 install flask requests python-whois qrcode --break-system-packages
```

### 3. Install & Set Up Ngrok

```bash
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
rm ngrok-stable-linux-amd64.zip
chmod +x ngrok
```

### 4. Authenticate Ngrok (REQUIRED or you'll get `ERR_NGROK_4018`)

```bash
./ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

---

##  LAUNCH MODE (RECOMMENDED)

From inside `SCAMTRACK/SCAMTRACK`:

```bash
python3 scamtrack_launcher.py
```

Then choose from:

* Start Flask Trap Server
* Launch Ngrok Tunnel
* View Logs in Terminal
* Generate QR Code
* Build Custom Payload
* Investigate Scam Domain

>  NOTE: Flask and Ngrok still require separate terminal windows for now. Background support coming soon.

---

##  INCLUDED PAYLOADS

| Payload                   | Description                                           |
| ------------------------- | ----------------------------------------------------- |
| `ip_grabber.html`         | Logs IP, headers, timezone, screen size, browser info |
| `clipboard_stealer.js`    | Attempts clipboard extraction                         |
| `device_fingerprint.html` | Logs OS, fonts, screen, battery, resolution, language |
| `screenshot_captor.html`  | Captures viewport using `html2canvas`                 |
| `bait_redirect.html`      | Logs and then redirects (e.g., to PayPal or Gmail)    |
| `deep_recon.html`         | Loads scam infra inside iframes for passive intel     |
| `app_launcher.html`       | Triggers URI schemes like `intent://`, `tel:`, etc.   |
| `*_trap.html`             | Generated payloads with redirect support              |

---

##  UTILITIES

| Tool                     | Description                                          |
| ------------------------ | ---------------------------------------------------- |
| `qr_generator.py`        | Generates QR codes from payload URLs                 |
| `payload_generator.py`   | Builds custom traps with optional redirects          |
| `scam_domain_tracker.py` | WHOIS + redirect + IP tracker for suspicious domains |
| `view_logs.py`           | Live tail of trap logs in terminal                   |
| `logs/`                  | JSON + text logs of trap hits                        |

---

## MANUAL TRAP DEPLOYMENT (ADVANCED)

### 1. Run Flask Server

```bash
cd SCAMTRACK/SCAMTRACK
python3 -m server.flask_server
```

Flask will start at:

```
http://localhost:5000
```

---

### 2. In a New Terminal, Start Ngrok

```bash
cd SCAMTRACK/SCAMTRACK
./ngrok http 5000
```

You’ll get a public URL like:

```
https://abc123.ngrok.app → http://localhost:5000
```

---

### 3. Send a Trap Link

Example payload:

```
https://abc123.ngrok.app/payloads/ip_grabber.html
```

---

##  BUILD A CUSTOM TRAP

```bash
cd SCAMTRACK/SCAMTRACK
python3 payload_generator.py
```

* Name it (`phishbait`)
* Add redirect (optional)
* It outputs: `payloads/phishbait_trap.html`

---

##  CREATE A QR CODE

```bash
cd SCAMTRACK/SCAMTRACK
python3 qr_generator.py
```

* Paste your payload URL
* Output: `payloads/scamtrack_qr.png`

---

##  LOGGING OPTIONS

* All logs stored in `/logs/` (JSON + .txt)
* Live view:

```bash
cd SCAMTRACK/SCAMTRACK
python3 view_logs.py
```

* Optional Discord alerts via:
  `server/webhook_reporter.py`

---

## ETHICAL DISCLAIMER

SCAMTRACK is for **ethical use only**.
Use only on systems and domains you **own or have explicit permission to test**.

---

**xoxo, ek0mssavi0r**

---

![Trap Screenshot](https://github.com/user-attachments/assets/33d3999d-c5e5-4824-be73-bcc5ffd7de41)

