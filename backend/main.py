
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
load_dotenv()
from backend.api.routes import router as api_router
from typing import Optional
from backend.agents import memory_agent as memory

app = FastAPI(title="LLM Multi-Agent Copilot System")

# Enable CORS so frontend can communicate with backend
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],  # In production, replace with specific domain
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# Simple health check
@app.get("/ping")
def ping():
	return {"message": "pong"}


# Serve static frontend files
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# Register all API routes under /api
app.include_router(api_router, prefix="/api")

# Add recall-memory endpoint
@app.get("/api/recall-memory")
def recall_memory_api(keyword: Optional[str] = Query(None), all: Optional[bool] = Query(False)):
	return memory.recall_memory(keyword=keyword, return_all=all)
