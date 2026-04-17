"""Minimal Gemini API test"""
import json, ssl, urllib.request, urllib.error, sys
print("=== Gemini API test ===", flush=True)

# Load key
key = None
with open(r"c:\Users\makar\Sync\oikos\01_ヘゲモニコン｜Hegemonikon\.env", "r") as f:
    for line in f:
        if line.strip().startswith("GOOGLE_API_KEY="):
            key = line.strip().split("=", 1)[1]
            break

if not key:
    print("No key found", flush=True)
    sys.exit(1)

print(f"Key: {key[:6]}...", flush=True)

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent?key={key}"
body = json.dumps({
    "contents": [{"parts": [{"text": "What is 2+2? Answer only the number."}]}],
    "generationConfig": {"temperature": 0, "maxOutputTokens": 10}
}).encode()

print("Calling API...", flush=True)
try:
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"}, method="POST")
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
        r = json.loads(resp.read().decode())
    text = r["candidates"][0]["content"]["parts"][0]["text"]
    print(f"Response: [{text.strip()}]", flush=True)
    print("SUCCESS", flush=True)
except urllib.error.HTTPError as e:
    b = e.read().decode()[:300] if e.fp else ""
    print(f"HTTP {e.code}: {e.reason}\n{b}", flush=True)
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}", flush=True)
