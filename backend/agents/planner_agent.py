

import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()

def run_planner(user_input: str):
	# 1. Try OpenAI if API Key exists
	api_key = os.getenv("OPENAI_API_KEY")
	if api_key and api_key.startswith("sk-"):
		try:
			client = openai.Client(api_key=api_key)
			prompt = f"""
			You are a smart AI planner agent. Given a user command, decide which agents should be called from the following list: search, calendar, checklist, email. Return a JSON object with a 'tasks' array listing the agents to call (e.g. ["search", "calendar"]), and a 'planner_output' string summarizing your reasoning.
			User command: {user_input}
			"""
			response = client.chat.completions.create(
				model="gpt-4o-mini", # or gpt-3.5-turbo
				messages=[
					{"role": "system", "content": "You are a helpful planner agent. Return ONLY valid JSON."},
					{"role": "user", "content": prompt}
				],
				max_tokens=150
			)
			reply = response.choices[0].message.content
			# Cleanup markdown code blocks if present
			if "```json" in reply:
				reply = reply.split("```json")[1].split("```")[0].strip()
			elif "```" in reply:
				reply = reply.split("```")[1].strip()
				
			return json.loads(reply)
		except Exception as e:
			print(f"OpenAI Error: {e}")
			pass # Fallthrough to next method

	# 2. Try Local Ollama
	try:
		client = openai.Client(
			api_key="ollama",
			base_url="http://localhost:11434/v1"
		)
		prompt = f"""
		Return a JSON object with keys 'tasks' (list of agents: search, calendar, checklist, email) and 'planner_output'.
		User command: {user_input}
		"""
		response = client.chat.completions.create(
			model="mistral",
			messages=[
				{"role": "system", "content": "You are a helpful planner agent. Output JSON only."},
				{"role": "user", "content": prompt}
			],
			max_tokens=150
		)
		reply = response.choices[0].message.content
		if "```json" in reply:
			reply = reply.split("```json")[1].split("```")[0].strip()
		elif "```" in reply:
			reply = reply.split("```")[1].strip()
		return json.loads(reply)
	except Exception as e:
		print(f"Ollama Error: {e}")
		pass

	# 3. Fallback: Keyword Matching (Demo Mode)
	tasks = []
	lower_input = user_input.lower()
	
	if "search" in lower_input or "find" in lower_input or "look up" in lower_input or "what is" in lower_input or "who is" in lower_input:
		tasks.append("search")
	
	if "email" in lower_input or "send" in lower_input or "mail" in lower_input:
		tasks.append("email")
		
	if "schedule" in lower_input or "calendar" in lower_input or "remind" in lower_input or "book" in lower_input or "plan" in lower_input:
		tasks.append("calendar")
		tasks.append("search") # assume planning needs info
		
	if "list" in lower_input or "todo" in lower_input or "check" in lower_input:
		tasks.append("checklist")

	# Default if nothing matches
	if not tasks:
		return {
			"planner_output": "I'm running in Demo Mode (no AI connected). I didn't recognize any keywords in your request. Try 'plan a trip', 'search for x', or 'send email'.",
			"tasks": []
		}

	return {
		"planner_output": f"I'm running in Demo Mode (no AI connected). Based on keywords, I've activated: {', '.join(tasks)}.",
		"tasks": tasks
	}
