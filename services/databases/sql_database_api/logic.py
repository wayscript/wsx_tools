import os

import mysql.connector
from mysql.connector import Error

# These values below come from your database credentials page.

host = os.environ.get('host')
user = os.environ.get('user')
password = os.environ.get('password')
database = os.environ.get('database')
port = '3306'#

### Helper functions
## Create database connection
# Takes credentials from your secrets file and connects to your database
# returns the connection
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
    except Error as e:
        return e

    return connection

# Read query
# reads no parameter querys from the SQL directory
def read_query(file_name):
    with open('sql/' + str(file_name), 'r') as f:
        query = f.read()
        return query

# Read Query with Params
# if your SQL statement needs dynamic parsing from data with the post request,
# this function will parse the query together to be returned
def read_query_with_params(file_name, table=None, column=None, value=None):
    with open('sql/' + str(file_name), 'r') as f:
        contents = f.readlines()
        if table and column and value:
            query = contents[0].format(table=table, column=column, value=value)
        if table and column and not value:
            query = contents[0].format(table=table, column=column)
        if table and not column and value:
            query = contents[0].format(table=table, value=value)
        if table and not column and not value:
            query = contents[0].format(table=table)
        return query

# insert data statement
def read_query_insert_data(file_name, table=None, value=None):
    with open('sql/' + str(file_name), 'r') as f:
        contents = f.readlines()
        if table and value:
            query = contents[0].format(table=table, value=value)
        return query

# Execute Query and return results
# Takes a query generated from an above helper function and executes it
# then the response is return to be used in the JSON response
def execute_and_return(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        return results
    except Error as e:
        print(e)
        return e

def execute_and_commit(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
