# qr_generator.py
import qrcode
import os

def generate_qr():
    print("🎯 SCAMTRACK QR Generator\n")
    url = input("Paste your full Ngrok trap URL (e.g., https://xxxx.ngrok.app/payloads/ip_grabber.html): ").strip()
    
    if not url.startswith("http"):
        print("❌ Invalid URL.")
        return

    filename = input("Output filename (default: scamtrack_qr.png): ").strip()
    if not filename:
        filename = "scamtrack_qr.png"
    if not filename.endswith(".png"):
        filename += ".png"

    img = qrcode.make(url)
    output_path = os.path.join("payloads", filename)
    img.save(output_path)

    print(f"✅ QR code saved to: payloads/{filename}")

if __name__ == "__main__":
    generate_qr()
