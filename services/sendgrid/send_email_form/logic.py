import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Check API Keys
def check_api_tokens(provided_token, accepted_tokens):
    provided_token_value = os.environ.get(str(provided_token))
    if isinstance( accepted_tokens, list ):
        accepted_tokens = [os.environ.get(token) for token in accepted_tokens]
        if provided_token in accepted_tokens:
            return True
    else:
        if provided_token_value == os.environ.get(accepted_tokens):
            return True
        else:
            return False

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
