import os

from flask import Flask, render_template, request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from logic import check_api_tokens, send_sendgrid_email

## Configuration:
## In Accepted Tokens, provide the NAMES of keys in .secrets
## that you want to have access to your tool.
accepted_tokens = ['DerricksToken1234', 'NiharsToken1234']

from_email = 'Derrick+testing@wayscript.com'

# App Logic
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/send_email', methods = ['GET', 'POST'])
def form_submit():
    if request.method == 'POST':
        to_email        = request.form.get('to_email')
        subject         = request.form.get('subject')
        content_to_send = request.form.get('content_to_send')
        api_token       = request.form.get('api_token')

        if check_api_tokens(api_token, accepted_tokens):
            response = send_sendgrid_email(from_email, to_email, subject, content_to_send)
            return response
        else:
            return 'Invalid API Key'
    else:
        return 'Not a valid request, Please Send POST.'

if __name__ == '__main__':
    app.run()
