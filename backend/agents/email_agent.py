import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def run_email(user_input: str) -> dict:
	sender_email = "anjutambe987@gmail.com"
	app_password = os.getenv("GMAIL_APP_PASSWORD")

	if not app_password:
		return {"email_result": "Failed to send email: GMAIL_APP_PASSWORD is not set in .env"}

	receiver_email = "anjutambe987@gmail.com"
	subject = "Multi-Agent Copilot Task"
	body = f"Details: {user_input}"

	msg = MIMEMultipart()
	msg['From'] = sender_email
	msg['To'] = receiver_email
	msg['Subject'] = subject
	msg.attach(MIMEText(body, 'plain'))

	try:
		# Connect to Gmail's SMTP server
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(sender_email, app_password)
		server.send_message(msg)
		server.quit()

		return {"email_result": "Email sent successfully via Gmail SMTP!"}
	except Exception as e:
		return {"email_result": f"Failed to send email via Gmail: {str(e)}"}
