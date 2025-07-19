# scam_domain_tracker.py
import socket
import requests
import whois
import json
import os
from datetime import datetime, timezone

def scam_recon():
    print("🔎 SCAMTRACK Domain Recon\n")
    domain = input("Enter suspicious domain or link (e.g., paypal-help.cc): ").strip()

    # Clean domain for filename & DNS resolution
    cleaned_domain = domain.replace("https://", "").replace("http://", "").replace("/", "")
    report = {
        "domain": domain,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    try:
        ip = socket.gethostbyname(cleaned_domain)
        report["resolved_ip"] = ip
    except:
        report["resolved_ip"] = "Resolution failed"

    try:
        whois_info = whois.whois(cleaned_domain)
        report["whois"] = {
            "registrar": whois_info.registrar,
            "creation_date": str(whois_info.creation_date),
            "expiration_date": str(whois_info.expiration_date),
            "emails": whois_info.emails
        }
    except:
        report["whois"] = "WHOIS failed"

    try:
        r = requests.get(f"https://ipapi.co/{report['resolved_ip']}/json", timeout=5)
        report["geoip"] = r.json()
    except:
        report["geoip"] = "GeoIP failed"

    # Ensure logs folder exists
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Sanitize filename
    clean_name = cleaned_domain.replace(".", "_")
    filename = f"logs/{clean_name}_recon.json"

    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\n✅ Recon report saved to: {filename}")

if __name__ == "__main__":
    scam_recon()
