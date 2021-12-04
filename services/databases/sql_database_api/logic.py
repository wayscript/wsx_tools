import os

import mysql.connector
from mysql.connector import Error

host_name = 'z5zm8hebixwywy9d.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'#os.environ.get('host')
user_name = 'zqrobp21lm3a28u3'#os.environ.get('user')
password = #os.environ.get('password')
database = 'o8mw8z2mfdko3zj2'#os.environ.get('database')
port = '3306'#

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=password,
            port=port,
            database=database
        )
    except Error as e:
        return e

    return connection

def read_query(file_name):
    with open('sql/' + str(file_name), 'r') as f:
        query = f.read()
        return query

def execute_and_return(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results
