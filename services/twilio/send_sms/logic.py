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

def send_twilio_sms(number_from, number_to, body):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body=body,
             from_=number_from,
             to=number_to
         )
    return message
