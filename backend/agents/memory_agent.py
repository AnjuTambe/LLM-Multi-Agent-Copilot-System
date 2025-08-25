# Handles short/long-term memory

# In-memory storage (for simplicity)
import datetime

# In-memory memory store
memory_store = []

def store_memory(query, results):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "query": query,
        "results": results
    }
    memory_store.append(entry)

def recall_memory(keyword=None, return_all=False):
    if return_all:
        return memory_store[-10:]  # limit to last 10
    elif keyword:
        matches = []
        for memory in reversed(memory_store):
            if keyword.lower() in str(memory["query"]).lower() or keyword.lower() in str(memory["results"]).lower():
                matches.append(memory)
        if matches:
            return matches
        return [{"error": f"No match found for keyword: {keyword}"}]
    elif memory_store:
        return [memory_store[-1]]  # last memory
    else:
        return [{"error": "No memory found."}]
