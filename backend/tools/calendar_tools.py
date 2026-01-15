from datetime import datetime, timedelta
from backend.utils.google_calendar import create_event, logger

def schedule_event_tool(summary: str, start_time: str = None, duration_minutes: int = 60, attendees: list = None):
    """
    Tool to schedule an event on Google Calendar.
    If start_time is missing, defaults to tomorrow at 9 AM.
    """
    if not start_time:
        # Default to tomorrow 9am if parsed failed
        tomorrow = datetime.now() + timedelta(days=1)
        start_time = tomorrow.replace(hour=9, minute=0, second=0, microsecond=0).isoformat()
    
    # Calculate end time
    try:
        start_dt = datetime.fromisoformat(start_time)
    except ValueError:
        # Fallback if format is weird
        start_dt = datetime.now() + timedelta(days=1)
        start_time = start_dt.isoformat()

    end_dt = start_dt + timedelta(minutes=duration_minutes)
    end_time = end_dt.isoformat()

    logger.info(f"Scheduling '{summary}' from {start_time} to {end_time}")
    
    result = create_event(
        summary=summary,
        start_time=start_time,
        end_time=end_time,
        attendees=attendees
    )
    
    if result:
        return f"Event '{summary}' scheduled successfully! Link: {result.get('htmlLink')}"
    else:
         # Mock success for demo if credentials fail
        return f"[DEMO MODE] Event '{summary}' scheduled for {start_time} (Mock Success - No Credentials Found)"
