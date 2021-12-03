import os

import mysql.connector
from mysql.connector import Error

host_name = os.environ.get('host')
user_name = os.environ.get('user')
password = os.environ.get('password')
database = os.environ.get('database')

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=password,
            database=database
        )
    except Error as e:
        return e

    return connection

def read_query(file_name):
    with open('sql/' + str(file_name)) + '.sql' as f:
    query = f.readlines()
    return query
