# SQL Database API

This service allows you to connect to your hosted database, query against your database, and add data to it via API endpoints hosted on WayScript.

## How It Works

This service works by connecting to your database via [MySQL Connector Python Library](https://dev.mysql.com/doc/connector-python/en/).

This requires being able to access your database credentials, including Database name, User, Password, and Host URL.

The API runs off a flask application, where you can retrieve and post data to different api URL endpoints via POST payloads.

The flask application parses together your payload into an SQL statement to execute against your connected database.

## Requirements
Hosted Database with access to database credentials.

## Setup
1. Download all files in the github repo
2. Upload to a WSX Lair

## Examples
```python
# Example of API Route Setup

# Get all tables of Database
@app.route('/get_tables', methods = ['GET'])
def get_tables():
    # Creation Connection and Query:
    connection = create_connection()
    query = read_query('get_tables.sql')
    # Execute Statement
    results = execute_and_return(connection, query)
    return {'results':results}
```
The above is an example setup of getting information from a database, getting all tables. Upon request, an SQL statement is read and executed against your connected database.
```python
# Query Specific Entry VIA POST
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
```
Other routes receive payload data from your POST request and parse these values into an SQL statement to be executed against your database. This specific example takes payload data of table, column, and value, and executes a SELECT statement against your database.
