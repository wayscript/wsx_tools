import requests
from flask import Flask, request

app = Flask(__name__)

# TODO
WAYSCRIPT_DEPLOY_TRIGGER_URL = 'https://volcanic-polygon-world-dev.wayscript.cloud'

#### RECEIVE MESSAGES FROM SLACK CHANNEL FUNCTIONALTY #####
# Slack App -> Features -> Event Subscriptions ( Toggle on )
# Set the wayscript endpoint to publically accessible ( Endpoints button on left bar within wayscript app )
# This endpoint will receive messages posted into slack that mention our bot
# When prompted to invite your bot to the connected channel, make sure to invite it (It will auto join)

@app.route('/', methods=['GET', 'POST'])
def receive_slack():
    if request.method == 'POST':
        if request.json:
            data = request.get_json()

            # For our connection, we must verify to slack our Endpoint
            # This logic will only be used upon the initial connection of our slack application
            if data.get('challenge'):
                return {'challenge' : data.get('challenge')}

            # This will be the logic we will use for creating events after our bot is triggered
            else:
                event = data.get('event')
                # the event json can be found under the examples directory, so you can find the info needed for your use case
                message = event.get('text')

                # We can set up any action for our bot here.
                # in this example we'll just send a message back to our slack channel using the second tool
                # if a certain word is found in the message
                if 'activate' in message:
                    send_message_url = WAYSCRIPT_DEPLOY_TRIGGER_URL + '/send-message'
                    payload = {"text" : message }
                    response = request.post(send_message_url, json=payload)
    else:
        return {'response' : 'please send post'}


#### SEND MESSAGE TO SLACK FUNCTIONALITY #####
# Slack App -> Features -> Incoming Webhooks ( Toggle On )
# This endpoint uses slack's webhook url to send messages to your flask application
# To send messages, you need to add a webhook into your slack app
# Webhooks can be added at the url https://api.slack.com/apps/<app_id>/incoming-webhooks?
# From this page, click 'Add a webhook' button
# Then select the channel you want to post messages to and click 'Allow'
# This will general a webhook url. Copy this address and paste it to the value below
# Example: slack_webhook_url = 'https://hooks.slack.com/services/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'

# To use the endpoint we're creating below, we must send a POST with a 'text' payload.
@app.route('/send-message', methods=['GET', 'POST'])
def send_message_to_slack():
    # Set this variable equal to the webhook url created from slack (View above instructions)
    slack_webhook_url = 'https://hooks.slack.com/services/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'

    if request.method == 'POST':
        if request.json:
            data = request.get_json()
            text = data.get('text', 'No text received from post request')
            json_data = {"text" : text}
            response = requests.post(slack_webhook_url, json=json_data)
            return {'response' : str(response.status_code) }
        else:
            # These lines of code are optional and can be changed for your desired error handling
            # Error when no payload is received
            return {"Error" : "No payload received with post request"}
    else:
        return {"Error" : "Request sent was not a POST request"}


if __name__ == '__main__':
    app.run()
