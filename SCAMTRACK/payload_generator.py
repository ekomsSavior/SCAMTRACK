# payload_generator.py
import os

def generate_payload():
    print("🎯 SCAMTRACK Payload Generator\n")
    payload_type = input("Payload type (e.g., ip, fingerprint, clipboard, custom_name): ").strip().lower()
    redirect_url = input("Redirect after logging? (leave blank to skip): ").strip()

    filename = f"payloads/{payload_type}_trap.html"

    with open(filename, 'w') as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
  <title>Verifying...</title>
  <script>
    const data = {
      userAgent: navigator.userAgent,
      language: navigator.language,
      platform: navigator.platform,
      timestamp: new Date().toISOString()
    };

    fetch("/tracker/%s", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
""" % payload_type)

        if redirect_url:
            f.write(f"""
    setTimeout(() => {{
      window.location.href = "{redirect_url}";
    }}, 1500);
""")

        f.write("""  </script>
</head>
<body>
  <h3>Verifying...</h3>
</body>
</html>""")

    print(f"\n✅ Payload saved as: {filename}")

if __name__ == "__main__":
    generate_payload()
