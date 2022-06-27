# Twilio-WayScript API
import os
from twilio.rest import Client
#from wayscript import context
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def send_message():
    if request.method == 'POST':
        sid = os.environ.get('sid')
        auth = os.environ.get('auth')

        data = request.get_json()
        if data.get('body') is None or data.get('to') is None:
            return 'Key "body" or "to" not defined.'
        if not sid or not auth:
            return 'Missing SID or Auth token'

        client = Client(sid, auth)
        msg_to = data.get('to')
        msg_body = data.get('body')
        message = client.messages \
            .create(
                 body=msg_body,
                 from_='+18644001062',
                 to=msg_to
             )
        print(message.sid)
        return 'Message Sent to {}'.format(msg_to)

if __name__ == '__main__':
    app.run()
