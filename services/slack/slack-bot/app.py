# WayScript Slack Application built on top of the slack API
# The routes below give access to slack resources without needing to pass a bearer token in the requests
# This allows system administrators to place credentials into a wayscript environment,
# rather than distributing keys to the users of your tools.
# security, logs, metrics, etc. are managed by wayscript.

# Configuration in WayScript:
# 1. Create a secret of bot_oauth_token with your slack provided bot token.
# This value should look like xoxb-...

# 2. Create a secret of signing_secret with your slack signing secret


import os

import requests
import hmac
from flask import Flask, render_template, request

# Helper Functions
# Returns your bearer token stored in your .secrets file
def build_auth_headers():
    bot_oauth_token = os.environ.get('bot-token')
    headers = {'Authorization': f'Bearer {bot_oauth_token}'}
    return headers

#returns your signing secret stored in your .secrets file
def get_signing_secret():
    signing_secret = os.environ.get('signing_secret')
    return signing_secret

def slack_verify(request):
    challenge = str(request.json.get('challenge'))
    timestamp = request.headers['X-Slack-Request-Timestamp']
    slack_signature = request.headers['X-Slack-Signature']
    request_body = request.data
    signing_secret = get_signing_secret()
    sig_basestring = 'v0' + str(timestamp) + ':' + str(request_body)
    my_signature = 'v0=' + hmac.compute_hash_sha256(
    slack_signing_secret,
    sig_basestring
    ).hexdigest()
    return hmac.compare_digest(my_signature, slack_signature)

# App Logic
app = Flask(__name__)

# Template Pages - Use these to create forms
@app.route('/')
def index():
    return render_template('index.html')

# Custom API Tools
@app.route('/get_channels', methods = ['GET', 'POST'])
def get_channels():
    headers = build_auth_headers()
    response = requests.get('https://slack.com/api/conversations.list', headers=headers)
    channels = []
    channel_ids = []
    data = response.json().get('channels')
    for i in data:
        channels.append(i.get('name'))
        channel_ids.append(i.get('id'))
    return {'channels':channels, 'channel_ids' : channel_ids }

@app.route('/get_users', methods = ['GET', 'POST'])
def get_users():
    headers = build_auth_headers()
    response = requests.post('https://slack.com/api/users.list', headers=headers)
    users = []
    user_ids = []
    data = response.json().get('members')
    for i in data:
        users.append(i.get('name'))
        user_ids.append(i.get('id'))
    return {'users':users, 'user_ids' : user_ids }

# Requires Argument users
@app.route('/open_conversation', methods = ['GET', 'POST'])
def open_conversation():
    if request.method == 'POST':
        if request.json.get('users'):
            users = request.json.get('users')
            headers = build_auth_headers()
            response = requests.post('https://slack.com/api/conversations.open', data=data, headers=headers)
            return {'message': response.json }
        else:
            return {'message' : 'Missing Required Argument of users in payload.'}
    else:
        return {'message' : 'Invalid method. Please use a POST request.'}

# Requires channel and one of text/attachments/blocks
@app.route('/post_message', methods = ['GET', 'POST'])
def post_message():
    if request.method == 'POST':
        if request.json.get('channel'):
            if request.json.get('text'):
                content = 'text'
            if request.json.get('attachments'):
                content = 'attachments'
            if request.json.get('blocks'):
                content = 'blocks'
            if content:
                data = {
                'channel': str(request.json.get('channel')),
                content : str(request.json.get(content))
                }
            headers = build_auth_headers()
            response = requests.post('https://slack.com/api/chat.postMessage', data=data, headers=headers)
            timestamp = response.json().get('message').get('ts')
            success = response.json().get('ok')
            return {'message': success, 'timestamp' : timestamp }
        else:
            return {'message' : 'Missing Required Argument of channel and/or one of text/attachments/blocks in payload.'}
    else:
        return {'message' : 'Invalid method. Please use a POST request.'}

# required arguments channel, text, and ts (timestamp)
@app.route('/update_message', methods = ['GET', 'POST'])
def update_message():
    if request.method == 'POST':
        if request.json.get('channel') and request.json.get('ts') and request.json.get('text'):
            data = {
            'channel': str(request.json.get('channel')),
            'ts' : str(request.json.get('ts')),
            'text' : str(request.json.get('text'))
            }
            headers = build_auth_headers()
            response = requests.post('https://slack.com/api/chat.update', data=data, headers=headers)
            return {'message': response.json }
        else:
            return {'message' : 'Missing Required Argument of channel, ts, or text in payload.'}
    else:
        return {'message' : 'Invalid request. Please send POST.'}

# Verify route for setting up webhooks.
@app.route('/verify', methods = ['GET', 'POST'])
def verify():
    if request.json and slack_verify(request):
        return_json = {"challenge": request.json.get('challenge') }
        return return_json
    else:
        return 'invalid.'

if __name__ == '__main__':
    app.run()
