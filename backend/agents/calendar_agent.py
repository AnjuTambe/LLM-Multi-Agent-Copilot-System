import datetime
from backend.utils.google_calendar import create_event

# Calendar Agent:
def run_calendar(user_input: str):
	# Dynamically calculate "Tomorrow Morning at 10:00 AM" in real-time
	now = datetime.datetime.now().astimezone()
	tomorrow = now + datetime.timedelta(days=1)
	
	start_time = tomorrow.replace(hour=10, minute=0, second=0, microsecond=0).isoformat()
	end_time = tomorrow.replace(hour=11, minute=0, second=0, microsecond=0).isoformat()

	event = create_event(
		summary="Trip Planning Block",
		description=user_input,
		start_time=start_time,
		end_time=end_time,
		attendees=["anjutambe987@gmail.com"],
		calendar_id="primary",
		recurrence=None
	)
	if event and event.get('htmlLink'):
		return {
			"calendar_result": f"Event scheduled dynamically for tomorrow! Link: {event['htmlLink']}"
		}
	else:
		return {
			"calendar_result": "Failed to schedule event."
		}
