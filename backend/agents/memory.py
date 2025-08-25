# backend/agents/memory.py
from typing import Optional, List

memory_store: List[dict] = []

def store_memory(query: str, results: dict):
    memory_store.append({
        "query": query,
        "results": results
    })

def recall_memory(keyword: Optional[str] = None) -> Optional[dict]:
    if not memory_store:
        return {"message": "No memory stored yet."}

    if keyword:
        for entry in reversed(memory_store):
            if keyword.lower() in entry["query"].lower():
                return entry
        return {"message": f"No memory found for keyword: {keyword}"}

    # Return the most recent memory
    return memory_store[-1]
