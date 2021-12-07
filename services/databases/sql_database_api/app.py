import os

from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error

from logic import ( create_connection, read_query, execute_and_return,
                    read_query_with_params, read_query_insert_data,
                    execute_and_commit )
from response_cleaner import clean_columns

## Configuration:

# App Logic
app = Flask(__name__)

# Index page - Accessed through templates/index.html
# The included example used the index as a crude API reference, can change
# this easily by changing index.html to suit your own needs.
@app.route('/')
def index():
    return render_template('index.html')

### Get Requests
# Get all tables of Database
@app.route('/get_tables', methods = ['GET'])
def get_tables():
    # Creation Connection and Query:
    connection = create_connection()
    query = read_query('get_tables.sql')
    # Execute Statement
    results = execute_and_return(connection, query)
    return {'results':results}

### Post Requests - Get Data
# Get table columns
# Parameters:
# table (Required) - the specified table to retrieve the columns of
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
            return {'results':'Error. Please send valid post request.'}

# Get all table data
# Parameters:
# table (Required) - the specified table to retrieve the data from
@app.route('/get_all_from_table', methods = ['GET', 'POST'])
def get_all_from_table():
    if request.method == 'POST':
        # Request Parameters
        # post request requires a table key i.e. {'table':'users'}
        data = request.get_json()
        table = data.get('table')
        # Creation Connection and Query:
        connection = create_connection()
        query = read_query_with_params('get_all_from_table.sql', table)
        # Execute Statement
        results = execute_and_return(connection, query)
        return {'results':results}
    else:
        return {'results':'Error. Please send valid post request.'}

@app.route('/get_entry_from_table', methods = ['GET', 'POST'])
def get_entry_from_table():
    # Pulling payload
    if request.method == 'POST':
        if request.json:
            data = request.get_json()
            table = data.get('table')
            column = data.get('column')
            value = data.get('value')
            # Creation Connection and Query:
            connection = create_connection()
            query = read_query_with_params('get_entry_from_table.sql', table, column, value)
            # Execute Statement
            results = execute_and_return(connection, query)
            return {'results':results}

### Post Requests - ADD data
# Create an entry in a specified table
# Parameters:
# table (Required) - The db table to add data to
# values (Required) - The values to add to the table i.e. '(24, "Derrick", 25)'
@app.route('/create_entry', methods = ['GET', 'POST'])
def create_entry():
    if request.method == 'POST':
        if request.json:
            data = request.get_json()
            table = data.get('table')
            value = data.get('value')
            # Creation Connection and Query:
            connection = create_connection()
            query = read_query_insert_data('insert_data.sql', table, value)
            # Execute Statement
            results = execute_and_commit(connection, query)
            return {'results':results}
        else:
            return {'results':'No payload received. Please include table and values'}
    else:
        return {'results':'Error. Please send valid post request.'}

if __name__ == '__main__':
    app.run()
