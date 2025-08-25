
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")  # Store this in .env

def run_email(user_input: str) -> dict:
	message = Mail(
		from_email='tambeanju987@gmail.com',  # ✅ Must match a verified sender in SendGrid
		to_emails='tambeanju987@gmail.com',
		subject='Multi-Agent Copilot Task',
		plain_text_content=f"Details: {user_input}"
	)

	try:
		sg = SendGridAPIClient(SENDGRID_API_KEY)
		response = sg.send(message)
		return {
			"email_result": f"Email sent successfully. Status Code: {response.status_code}"
		}
	except Exception as e:
		return {
			"email_result": f"Failed to send email: {str(e)}"
		}
