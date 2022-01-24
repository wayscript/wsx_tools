# Method chat.update

# Required Scopes
# Bot tokens : [ chat:write ]
# User Tokens : [chat:write, chat:write:bot, chat:write:user]

# Required Arguments:
# Bearer Token
# channel - channel ID containing message to be updated ( i.e. CTZB4KTKP)
# ts - timestamp of message to be updated ( i.e. 1642974858.000400 )

# If you are unsure of your channel id, use get_channels.py script.

import requests
import os

bot_oauth_token = os.environ.get('bot_oauth_token')

headers = {'Authorization': f'Bearer {bot_oauth_token}'}

data = {
'channel'   :   'CTZB4KTKP',
'ts'        :   '1642974858.000400',
'text'      :   'Edited from update_message.py'
}

response = requests.post('https://slack.com/api/chat.update', data=data, headers=headers)

print(response.content)
