import os
from twilio.rest import Client

account_sid = os.environ.get('sid')
auth_token = os.environ.get('auth')


client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+18644001062',
         to='+1'
     )

print(message.sid)
