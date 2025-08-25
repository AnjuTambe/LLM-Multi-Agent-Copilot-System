# Google Calendar event creation utility
import os
import pickle
import logging
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.events']
CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), 'credentials', 'credentials.json')
TOKEN_PATH = os.path.join(os.path.dirname(__file__), 'credentials', 'token.pickle')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def authenticate_google():
	creds = None
	if os.path.exists(TOKEN_PATH):
		with open(TOKEN_PATH, 'rb') as token:
			creds = pickle.load(token)
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
			creds = flow.run_local_server(port=0)
		with open(TOKEN_PATH, 'wb') as token:
			pickle.dump(creds, token)
	return creds

def create_event(
	summary,
	description="",
	start_time=None,
	end_time=None,
	attendees=None,
	calendar_id="primary",
	recurrence=None
):
	"""
	Create a Google Calendar event with advanced options.
	Args:
		summary (str): Event title
		description (str): Event description
		start_time (str): RFC3339 start datetime
		end_time (str): RFC3339 end datetime
		attendees (list): List of attendee emails
		calendar_id (str): Calendar ID
		recurrence (list): Recurrence rules
	Returns:
		dict: Created event details
	"""
	try:
		creds = authenticate_google()
		service = build('calendar', 'v3', credentials=creds)

		event = {
			'summary': summary,
			'description': description,
			'start': {
				'dateTime': start_time,
				'timeZone': 'America/Los_Angeles',
			},
			'end': {
				'dateTime': end_time,
				'timeZone': 'America/Los_Angeles',
			},
		}

		if attendees:
			event['attendees'] = [{'email': email} for email in attendees]
		if recurrence:
			event['recurrence'] = recurrence
		event['conferenceData'] = {
			'createRequest': {
				'requestId': 'meet-' + datetime.now().strftime('%Y%m%d%H%M%S'),
				'conferenceSolutionKey': {
					'type': 'hangoutsMeet'
				}
			}
		}

		created_event = service.events().insert(
			calendarId=calendar_id,
			body=event,
			conferenceDataVersion=1,
			sendUpdates="all"
		).execute()
		logger.info(f"Event created: {created_event.get('htmlLink')}")
		logger.info(f"Full event response: {created_event}")
		return created_event
	except Exception as e:
		logger.error(f"Failed to create event: {e}")
		return None
