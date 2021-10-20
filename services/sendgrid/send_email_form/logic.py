import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_sendgrid_email(from_email, to_email, subject, html_content):
    message = Mail(
        from_email = str(from_email),
        to_emails = str(to_email),
        subject = str(subject),
        html_content = str(html_content))
    try:
        sg = SendGridAPIClient(os.environ.get('sendgrid_api_token'))
        response = sg.send(message)
        return response
    except Exception as response:
        return response
