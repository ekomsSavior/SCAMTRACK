# SCAMTRACK

**Track. Trap. Trace.**
**by ekomsSavi0r**

![Trap Screenshot](https://github.com/user-attachments/assets/33d3999d-c5e5-4824-be73-bcc5ffd7de41)

SCAMTRACK is a one-click phishing trap generator and scammer tracker.

> Pair with [PHISH HUNTER PRO](https://github.com/ekomsSavior/PHISH_HUNTER_PRO) for full-spectrum scammer disruption.

---

## FEATURES

*  One-file CLI to launch Flask + Ngrok + Payload menu
*  QR code generator for instant trap delivery
*  Scam domain recon and WHOIS tools
*  Payloads for IP logging, screenshots, clipboard, and device fingerprinting and more.
*  Live terminal log viewer
*  Modular, fast, and noob-friendly
*  Module to add your own payloads into SCAMTRACKER


---

##  REQUIREMENTS

* Python 3.10+
* Kali Linux (or any Linux distro)
* Ngrok (Free or Personal Plan)

---

##  INSTALLATION

### 1. Clone the Repo

```bash
git clone https://github.com/ekomsSavior/SCAMTRACK.git
cd SCAMTRACK/SCAMTRACK
```

### 2. Install Dependencies

```bash
sudo apt update && sudo apt install -y python3 python3-pip unzip
pip3 install flask requests python-whois qrcode --break-system-packages
```

### 3. Install & Set Up Ngrok

```bash
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar -xvzf ngrok-v3-stable-linux-amd64.tgz
sudo mv ngrok /usr/local/bin/
```

### 4. Authenticate Ngrok

```bash
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

---

##  USAGE

###  One Command to Rule Them All

```bash
cd SCAMTRACK/SCAMTRACK
python3 scamtrack_cli.py
```

You'll be greeted with:

```
[1] Build Full Trap (Flask + Ngrok + Payload Picker)
[2] Upload Your Own Payload
[3] View Live Logs
[4] Recon a Suspicious Scam Domain
[5] Exit
```

---


###  Build Full Trap (Option 1)

* Auto-launches Flask trap server on port 5000
* Starts Ngrok tunnel instantly
* Offers payload picker with all available `.html` and `.js` files
* Option to chain multiple payloads into one flow
* NEW! Cloaks final URL using [is.gd](https://is.gd)
* Offers QR code generation for physical delivery

**You’ll see output like:**

```
 Starting Ngrok tunnel on port 5000...
 Ngrok Public URL: https://abc123.ngrok.app

 Available Payloads:
[1] app_launcher.html
[2] bait_redirect.html
[3] clipboard_stealer.js
[4] deep_recon.html
[5] device_fingerprint.html
[6] grabber.js
[7] ip_grabber.html
[8] screenshot_captor.html
[9] Chain Multiple Payloads

 Shortening URL via is.gd...
 Shortened: https://is.gd/kN0Pq7

 Your trap link is cloaked:
https://is.gd/kN0Pq7

 QR Code saved to:
scam_qr/login_error_qr.png
```

---

### Add your own Payload (Option 2)

follow the commands to integrate your payloads into the SCAMTRACK framework.

---

###  Real-Time Logs (Option 3)

* Shows trap hits live in terminal
* Logs IP, device, browser, time, and more

All events are saved to:

```
logs/tracker_events.log
```

---

###  Scam Recon (Option 4)

* Analyze suspicious domains
* Checks redirects, WHOIS, IP, and basic infra intel

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
| `*_trap.html`             | Custom traps with redirect support                    |

---

##  HOW SCAMTRACK WORKS (Behind the Scenes)

SCAMTRACK is more than a flashy CLI — it's a trap engine designed to *deliver and log payload activity* using a Flask web server and Ngrok tunnel.

Here’s exactly what happens when you launch a trap:

1. **Flask Trap Server Starts Locally**
   → SCAMTRACK runs a local Flask server on `http://localhost:5000`, ready to serve your HTML or JS-based payloads.
   → Payloads are hosted from the `/payloads/` folder — this includes things like `ip_grabber.html`, `clipboard_stealer.js`, etc.

2. **Ngrok Connects Your Localhost to the Internet**
   → SCAMTRACK auto-launches `ngrok http 5000`, which creates a **public HTTPS link** to your local trap server.
   → Example: `https://abc123.ngrok.app → http://localhost:5000`

3. **Payload is Tied to Public Link**
   → SCAMTRACK gives you a complete trap URL like:
   `https://abc123.ngrok.app/payloads/ip_grabber.html`
   → This URL is safe to send to scammers or load into QR codes.

4. **Victim Clicks the Trap**
   → When someone clicks your link or scans the QR code:

   * Flask serves the payload
   * JavaScript logs their IP, browser, OS, screen size, etc.
   * Logs are written in real-time to: `logs/tracker_events.log`

5. **Optional Logging + QR Code Creation**
   → SCAMTRACK auto-generates a QR code for the payload URL
   → Optional Discord alerts can be configured via `webhook_reporter.py`
   → You can watch hits in real-time using the `View Live Logs` option.

 All of this happens from a single command:

```bash
python3 scamtrack_cli.py
```
--- 

## ☠️ ETHICAL DISCLAIMER

SCAMTRACK is for **educational and defensive use only**.
You are fully responsible for how you use this tool.
Use only on systems and domains you **own** or have **explicit permission** to test.

---

🕷️ xoxo — ekomsSavi0r



