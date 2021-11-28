import os

from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error


from logic import create_connection

## Configuration:
os.environ.get('')

# App Logic
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Get Requests
@app.route('/get_tables', methods = ['GET'])
def get_tables():
    connection = create_connection("localhost", "root", "", "sm_app")





# Post Requests
@app.route('/create_table', methods = ['GET', 'POST'])
def form_submit():
    if request.method == 'POST':
        if request.form:
            to_email        = request.form.get('to_email')
            subject         = request.form.get('subject')
            content_to_send = request.form.get('content_to_send')
            api_token       = str(request.form.get('api_token'))
        if request.json:
            to_email        = request.json.get('to_email')
            subject         = request.json.get('subject')
            content_to_send = request.json.get('content_to_send')
            api_token       = str(request.json.get('api_token'))

        if api_token in accepted_tokens:
            response = send_sendgrid_email(from_email, to_email, subject, content_to_send)
            return 'success!'
        else:
            return 'Invalid Token - Contact System Admin'
    else:
        return 'Not a valid request, Please Send POST.'

if __name__ == '__main__':
    app.run()
