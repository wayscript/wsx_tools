import requests
import os

bot_oauth_token = os.environ.get('bot_oauth_token')

headers = {'Authorization': f'Bearer {bot_oauth_token}'}

response = requests.get('https://slack.com/api/conversations.list', headers=headers)
channels = []
channel_ids = []
data = response.json().get('channels')
for i in data:
    channels.append(i.get('name'))
    channel_ids.append(i.get('id'))

print(channels, channel_ids)
