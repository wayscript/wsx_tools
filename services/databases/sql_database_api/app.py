import os

from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error

from logic import create_connection, read_query, execute_and_return, read_query_with_params
from response_cleaner import clean_columns

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

@app.route('/get_all_from_table', methods = ['GET', 'POST'])
def get_all_from_table():
    if request.method == 'POST':
        # Request Parameters
        data = request.get_json()
        table = data.get('table')
        print(table)
        # Creation Connection and Query:
        connection = create_connection()
        query = read_query_with_params('get_all_from_table.sql', table)
        # Execute Statement
        results = execute_and_return(connection, query)
        return {'results':str(results)}

# Post Requests
@app.route('/get_entry_from_table', methods = ['GET', 'POST'])
def get_entry_from_table():
    # Pulling payload
    table = request.json('table')
    column = request.json('column')
    value = request.json('value')
    # Creation Connection and Query:
    connection = create_connection()
    query = read_query_with_params('get_entry_from_table.sql', table, column, value)
    # Execute Statement
    results = execute_and_return(connection, query)
    return {'results':str(results)}

# Post Requests
@app.route('/describe_table', methods = ['GET', 'POST'])
def describe_table():
    if request.method == 'POST':
        if request.json:
            # Receive data from the post request
            data = request.get_json()
            table = data.get('table')
            # Create connection to database
            connection = create_connection()
            # Read SQL file query
            query = read_query_with_params('describe_table.sql', table)
            # Execute and clean query response
            results = execute_and_return(connection, query)
            columns = clean_columns(results)
            return {'results':columns}
        else:
            return {'message':'Invalid method, please send POST'}


@app.route('/create_entry', methods = ['GET', 'POST'])
def create_entry():
    if request.method == 'POST':
        if request.json:
            data = request.get_json()
            table = data.get('table')
            values = data.get('values')
            # Creation Connection and Query:
            connection = create_connection()
            query = read_query_with_params('insert_customer.sql', table, None, values)
            # Execute Statement
            results = execute_and_return(connection, query)
            return {'results':str(results)}

if __name__ == '__main__':
    app.run()
