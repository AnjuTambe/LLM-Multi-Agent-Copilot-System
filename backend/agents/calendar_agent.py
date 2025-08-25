

from backend.utils.google_calendar import create_event


def run_calendar(user_input: str):
	# Example static values; replace with dynamic extraction from user_input as needed
	event = create_event(
		summary="Copilot Event",
		description=user_input,
		start_time="2025-08-22T10:00:00-07:00",
		end_time="2025-08-22T11:00:00-07:00",
		attendees=["tambeanju987@gmail.com"],
		calendar_id="primary",
		recurrence=None
	)
	if event and event.get('htmlLink'):
		return {
			"calendar_result": f"Event scheduled! Link: {event['htmlLink']}"
		}
	else:
		return {
			"calendar_result": "Failed to schedule event."
		}
