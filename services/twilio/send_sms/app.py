import os

from flask import Flask, render_template, request
from twilio.rest import Client

from logic import check_api_tokens, send_twilio_sms

## Configuration:
## In Accepted Tokens, provide the NAMES of keys in .secrets
## that you want to have access to your tool.
accepted_tokens = ['DerricksToken1234', 'NiharsToken1234']

# App Logic
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/send_email')
def form_submit():
    number_from     = request.args.get('from')
    number_to       = request.args.get('to')
    body            = request.args.get('body')
    api_token       = request.args.get('api_token')

    if check_api_tokens(api_token, accepted_tokens):
        response = send_twilio_sms(number_from, number_to, body)
        return response.status_code
    else:
        return "<h3>Form Invalid. Your API Key may of been revoked. Please Contact your Tool Administrator</h3>"

if __name__ == '__main__':
    app.run()
