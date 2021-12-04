import os

from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error


from logic import create_connection, read_query, execute_and_return

## Configuration:

# App Logic
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Get Requests
@app.route('/get_tables', methods = ['GET'])
def get_tables():
    # Creation Connection and Query:
    connection = create_connection()
    query = read_query('get_tables.sql')
    # Execute Statement
    results = execute_and_return(connection, query)
    return {'results':str(results)}

@app.route('/get_all_from_table', methods = ['GET'])
def get_all_from_table():
    # Creation Connection and Query:
    connection = create_connection()
    query = read_query('get_all_from_table.sql')
    # Execute Statement
    results = execute_and_return(connection, query)
    return {'results':str(results)}


# Post Requests
@app.route('/create_table', methods = ['GET', 'POST'])
def create_Table():
    if request.method == 'POST':
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

@app.route('/create_entry', methods = ['GET', 'POST'])
def create_entry():
    # Creation Connection and Query:
    connection = create_connection()
    query = read_query('insert_customer.sql')
    # Execute Statement
    results = execute_and_return(connection, query)
    return {'results':str(results)}

if __name__ == '__main__':
    app.run()
