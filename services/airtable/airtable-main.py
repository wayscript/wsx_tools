'''
Setup
API key credentials
Create Entry
Create Table
Update
Update All
Delete
'''

# pip install -r requirements.txt

# Modify these for your own project:

base_id = 'appyWAikEbS3b7Ejy'
# base_id comes from your url whenever working within your base, beginning with 'app'
# i.e. the url https://airtable.com/appyWAikEbS3b7Ejy/tblX4laQnvyytwrnN/viwUJVmlWQIK0jvTA?blocks=hide
# the base_id is 'appyWAikEbS3b7Ejy'

table_id = 'tblX4laQnvyytwrnN'
# table_id is the second string of your url when working within your table
# using the same sample from above, the table_id would be 'tblX4laQnvyytwrnN'

personal_access_token = 'pat1zGGcxgDBVmama.6d6249472f7ad775bfd5c3f3fb8ca6b5cae98d63f113689d8c69484e1d25a92b'
# This value is created by the user at https://airtable.com/create/tokens/new
# Be sure to add the appropriate scopes AND select the base you want the token to be used for
# if using WayScript, it is safer to store this value in your .secrets file and retrieve it in this script using os.environ.get(<name_of_secret>)
# This token gives access to your airtable account functionality, so do not share this value


#### Begin Project Code
import requests

def create_headers():
    headers = {
    'Authorization': 'Bearer ' + str(personal_access_token),
    'Content-Type': 'application/json',
    }
    return headers

base_table_api_url = 'https://api.airtable.com/v0/{}/{}'.format(base_id, table_id)

# 1. List current records from table
headers = create_headers()
response = requests.get(base_table_api_url, headers=headers)
print(response.json())

# 2. Create an Entry
headers = create_headers()
json_data = {
    'records': [
        {
            'fields': {
                'Name': 'Union Square',
                'Email': 'Union@gmail.com',
                'Product' : 'Tier 2',
                'Renewal Date': '11/29/2023',
                'Additional Info' : ''
            },
        },
    ],
}
response = requests.post(base_table_api_url, headers=headers, json=json_data)
print(response.content)

# Update a record
headers = create_headers()
json_data = {
            'fields': {
                'Name': 'Union Square',
                'Email': 'Union@gmail.com',
                'Product' : 'Tier 3',
                'Renewal Date': '11/29/2023',
                'Additional Info' : ''
            },
            }
record_id = 'rec0JR0B9qsB3JWzn'
#record_id is found by expanding the record, or by retrieving it programmatically
response = requests.put(base_table_api_url+ '/' + record_id, headers=headers, json=json_data)
print(response.content)

# Delete a record
headers= create_headers()
record_id = 'rec0JR0B9qsB3JWzn'
response = requests.delete(base_table_api_url+ '/' + record_id, headers=headers)
