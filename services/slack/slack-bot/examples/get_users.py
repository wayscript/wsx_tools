# Method users.list

# Required Scopes
# User Tokens : [ user:read ]
# Bot Tokens : [ user:read ]

# Required Arguments:
# Bearer Token

import requests
import os

bot_oauth_token = os.environ.get('bot_oauth_token')

headers = {'Authorization': f'Bearer {bot_oauth_token}'}

response = requests.post('https://slack.com/api/users.list', headers=headers)
# pulling users
users = []
user_ids = []
data = response.json().get('members')
for i in data:
    users.append(i.get('name'))
    user_ids.append(i.get('id'))

print(users, user_ids)
