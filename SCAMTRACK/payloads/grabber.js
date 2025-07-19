(async () => {
  const data = {
    userAgent: navigator.userAgent,
    language: navigator.language,
    platform: navigator.platform,
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
    screen: {
      width: screen.width,
      height: screen.height,
      colorDepth: screen.colorDepth
    },
    timestamp: new Date().toISOString()
  };

  try {
    // Grab public IP using a reliable free API
    const ipRes = await fetch("https://api.ipify.org?format=json");
    const ipData = await ipRes.json();
    data.ip = ipData.ip;
  } catch (e) {
    data.ip = "Unavailable";
  }

  // Send it to our Flask trap
  fetch("/tracker/ip", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
})();
