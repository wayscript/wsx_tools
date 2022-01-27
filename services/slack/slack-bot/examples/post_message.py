# Method chat.postMessage

# Required Scopes
# Bot tokens : [ chat:write ]
# User Tokens : [chat:write, chat:write:bot, chat:write:user]

# Required Arguments:
# Bearer Token
# channel - channel ID containing message to be updated ( i.e. CTZB4KTKP)
# text/attachments/blocks - one of these fields. Text used below.

import requests
import os

bot_oauth_token = os.environ.get('bot_oauth_token')

headers = {'Authorization': f'Bearer {bot_oauth_token}'}

data = {
'channel':'general',
'text':'Coming from bot'
}

response = requests.post(<DEPLOY_TRIGGER_ENDPOINT>/post_message, data=data, headers=headers)

timestamp = response.json().get('message').get('ts')
success = response.json().get('ok')
print(success, timestamp)
