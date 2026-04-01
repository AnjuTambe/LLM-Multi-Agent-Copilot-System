import os
import requests
from dotenv import load_dotenv

load_dotenv('/Users/anjali/Desktop/LLM_Project/LLM-Multi-Agent-Copilot-System/.env')
gemini_key = os.getenv("GEMINI_API_KEY")

payload = {
    "contents": [{"parts": [{"text": "Hello, what is AI?"}]}],
    "generationConfig": {"response_mime_type": "application/json"}
}
try:
    resp = requests.post(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gemini_key}", json=payload)
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.text}")
except Exception as e:
    print(f"Error: {e}")
