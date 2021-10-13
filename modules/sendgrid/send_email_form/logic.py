import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Check API Keys
def check_api_tokens(provided_token, accepted_tokens):
    provided_token_value = os.environ.get(str(provided_token))
    if isinstance( accepted_tokens, list ):
        accepted_token_values = []
        for token in accepted_tokens:
            token_value = os.environ.get(token)
            accepted_token_values.append(token_value)
        if provided_token_value in accepted_token_values:
            return True
        else:
            return False
    else:
        if provided_token_value == os.environ.get(accepted_tokens):
            return True
        else:
            return False

def send_sendgrid_email(from_email, to_email, subject, html_content, sendgrid_api_token):
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=html_content)
    try:
        sg = SendGridAPIClient(os.environ.get('sendgrid_api_token'))
        response = sg.send(message)
        return response
    except Exception as response:
        return response
