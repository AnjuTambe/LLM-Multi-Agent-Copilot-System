from typing import List, Dict, Any
from backend.tools.search_tools import web_search_tool
from backend.tools.calendar_tools import schedule_event_tool

def run_execution_agent(tasks: List[str], user_input: str) -> Dict[str, Any]:
    """
    Executes a list of tasks by calling appropriate tools.
    """
    results = {}
    
    for task in tasks:
        if task == "search":
            # Extract query from user_input (naive approach for demo)
            results["active_search"] = web_search_tool(user_input)
            
        elif task == "calendar":
            # Naive extraction for demo
            summary = "Meeting/Event"
            if "trip" in user_input: summary = "Trip Planning"
            elif "meeting" in user_input: summary = "Meeting"
            
            results["active_calendar"] = schedule_event_tool(summary=summary)
            
        elif task == "email":
            results["active_email"] = "Email draft prepared (Demo Mode)."
            
        elif task == "checklist":
             results["active_checklist"] = ["Item 1", "Item 2"]

    return results
