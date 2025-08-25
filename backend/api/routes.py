from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.agents.planner_agent import run_planner
from backend.agents.search_agent import run_search
from backend.agents.calendar_agent import run_calendar
from backend.agents.checklist_agent import run_checklist
from backend.agents.email_agent import run_email
from backend.agents.memory_agent import store_memory, recall_memory

router = APIRouter()

class AgentRequest(BaseModel):
	input: str




@router.post("/run-agent")
async def run_agent(request: AgentRequest):
	try:
		# Memory Recall Check
		if "recall" in request.input.lower() or "remember" in request.input.lower():
			return recall_memory()

		planner_response = run_planner(request.input)
		tasks = planner_response.get("tasks", [])
		results = {"planner": planner_response}

		if "search" in tasks:
			results["search"] = run_search(request.input)

		if "calendar" in tasks:
			results["calendar"] = run_calendar(request.input)

		if "checklist" in tasks:
			results["checklist"] = run_checklist(request.input)

		if "email" in tasks:
			results["email"] = run_email(request.input)

		# Store full results in memory after all agents finish
		store_memory(request.input, results)

		return {"output": results}

	except Exception as e:
		return {"error": str(e)}
