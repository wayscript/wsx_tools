# Slack Automation Service
This is a service to allow members of your team to interface with slack programmatically and easily.

## How it works:
This tool allows a system administrator of a slack workspace to create one bot. Then users are able to interface with that bot via wayscript.
This allows the system admin to only need one bot oauth token for the entire team to use slack bots.
Traditionally, ever member would need to go through the setup of a slack bot to use their own in a workspace, with wayscript this process
needs to happen once and all members can use. This lets you setup and manage your bot all from one place for everyone on your team.

To send bot messages with this tool:
<ul>
<li>Send POST requests to wayscript endpoint with WayScript account auth bearer tokens</li>
</ul>

## Requirements:
A Slack account, workspace, and app.

## Setup:
### Create a Lair
Lairs are preconfigured environments hosted by WayScript. To create a Lair, signin to wayscript and click " + New Lair."

### Upload files:
Download from GitHub and upload to WSX the files within slack-bot

### Setup Secrets
<p align="center">
  <img src="https://raw.githubusercontent.com/wayscript/wsx_tools/master/static/slack/bot-token.jpg" />
</p>

You will need to place yourslack provided api token into your wayscript .secrets file.
The name of this token should be ```bot-token```

This token can be found on your slack app page at:
https://api.slack.com/apps/<APP_ID>/oauth?

It will look like:
xoxb-...

Slack Tokens have corresponding scopes to their tokens. If you want to use every service in this repo, please use all the following scopes:
<p align="center">
  <img src="https://raw.githubusercontent.com/wayscript/wsx_tools/master/static/slack/SlackAPIScopes.jpg" />
</p>

### Host your Tool
Host your tool by creating a deploy trigger within your .triggers file

The command to run will be:
```Python
flask run --port 8080 --host 0.0.0.0
```
Port ```8080```
For additional help on running servers please see:
https://wsxdocs.wayscript.com/quickstart/host-a-flask-server

This will host your tool at the provided url in the trigger

A nice to have, if you want to make changes and have them immediately reflect in your flask application is to set an environment variable
```Python
FLASK_ENV = development
```
This enables hot reloading as you make changes to your files.

### Testing your tool
You can test your tool by visiting the url provided in your deploy trigger, or sending a request to the url.

A sample request may look like:
```Python
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
print(success, timestamp)'''

response = requests.post(url, json = data)
print(response.content)
```
