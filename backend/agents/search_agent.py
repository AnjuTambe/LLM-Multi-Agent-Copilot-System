import os
import requests

def run_search(query: str):
	gemini_key = os.getenv("GEMINI_API_KEY")
	
	if not gemini_key or gemini_key == "mock-key-for-demo":
		return {"search_results": [f"Mock Search for: {query} (No Real API Key built-in)"]}
		
	try:
		prompt = f"You are a specialized Web Search Agent. Your ONLY job is to extract the core topic from this user request and provide 3-5 real-world facts, places, or details. DO NOT mention your limitations, emails, or calendars. Just provide the information.\n\nUser request: '{query}'"
		payload = {
			"contents": [{"parts": [{"text": prompt}]}]
		}
		resp = requests.post(
			f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gemini_key}",
			json=payload
		)
		data = resp.json()
		reply = data["candidates"][0]["content"]["parts"][0]["text"].strip()
		return {
			"search_results": [reply]
		}
	except Exception as e:
		print(f"Gemini Search Error: {e}")
		return {"search_results": ["Failed to fetch online data."]}
# print(run_search("Seattle trip"))
