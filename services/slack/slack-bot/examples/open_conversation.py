# Method conversations.open

# Required Scopes
# Bot Tokens : [ channels:manage, groups:write, im:write, mpim:write ]
# User Tokens : [ channels:manage, groups:write, im:write, mpim:write ]

# Required Arguments:
# Bearer Token
# users

import requests
import os

bot_oauth_token = os.environ.get('bot_oauth_token')

headers = {'Authorization': f'Bearer {bot_oauth_token}'}

data = {
'users':'UTP6HS14H,U01FXLMCT62,U01G1A8C7EH,U01GAHL0LHJ,U02UWMR4VDG'
}

response = requests.post('https://slack.com/api/conversations.open', data=data, headers=headers)

print(response.content)
