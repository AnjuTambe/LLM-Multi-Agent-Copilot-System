# Multi-Agent Copilot System

A Python-based AI orchestration engine capable of asynchronous tool execution and sophisticated natural language processing. 

This project features a robust routing "Planner Engine" that evaluates natural language prompts and dynamically delegates execution to specialized, independent sub-agents.

## Core Features
*   **Planner Agent:** Parses natural language intent and routes execution to necessary sub-agents using the Gemini 2.5 Flash API.
*   **Search Agent:** Performs live, hyper-relevant web searches and summarizes real-world data points.
*   **Calendar Agent:** Integrates natively with the Google Calendar API via OAuth 2.0. Dynamically calculates localized UTC timestamps using Python's `datetime` module to autonomously schedule user events.
*   **Email Agent:** Automatically packages generated content and dispatches it directly to users via a native local `smtplib` interface.
*   **Resilient Fallback Mode:** Built-in error handling ensures the application gracefully degrades into an offline keyword-based fallback system if API rate limits are exhausted, guaranteeing zero crashes.

## Tech Stack
The backend is entirely powered by **Python**, **FastAPI**, and **Uvicorn**, which seamlessly serves an intuitive vanilla **HTML/CSS/JS** frontend UI.

## Local Setup
1. Clone the repository to your local machine.
2. Initialize and activate a Python virtual environment.
3. Install the required dependencies: `pip install -r backend/requirements.txt`
4. Create a `.env` file at the root of the project and secure your API credentials (`GEMINI_API_KEY` and `GMAIL_APP_PASSWORD`).
5. Create a Google Cloud Project, activate the Calendar API, and authorize an OAuth client. Download the `credentials.json` file to `backend/utils/credentials/`.
6. Launch the application: `python -m uvicorn backend.main:app --port 8000`
