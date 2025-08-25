

import openai

# Use Ollama’s OpenAI-compatible API
client = openai.Client(
    api_key="ollama",  # dummy value, required by the SDK
    base_url="http://localhost:11434/v1"
)


def run_planner(user_input: str):
	prompt = f"""
You are a smart AI planner agent. Given a user command, decide which agents should be called from the following list: search, calendar, checklist, email. Return a JSON object with a 'tasks' array listing the agents to call, and a 'planner_output' string summarizing your reasoning.

User command: {user_input}
"""
	try:
		response = client.chat.completions.create(
        model="mistral",
        messages=[
        {"role": "system", "content": "You are a helpful planner agent."},
        {"role": "user", "content": prompt}
        ],
         max_tokens=150
    )
		reply = response.choices[0].message.content
		import json
		try:
			result = json.loads(reply)
			return result
		except Exception:
			return {"planner_output": reply, "tasks": []}
	except Exception as e:
		return {"planner_output": f"Planner error: {e}", "tasks": []}
