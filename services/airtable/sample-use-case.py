'''
Clear Existing Data
Take Data from Source and POST to airtable
Update Airtable Data
'''

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

def create_headers():
    headers = {
    'Authorization': 'Bearer ' + str(personal_access_token),
    'Content-Type': 'application/json',
    }
    return headers

base_table_api_url = 'https://api.airtable.com/v0/{}/{}'.format(base_id, table_id)

# Get table records
import requests
import pandas as pd
import json

headers = create_headers()
response = requests.get(base_table_api_url, headers=headers)
table_record_ids = []
for i in response.json().get('records'):
    id = i.get('id')
    table_record_ids.append(id)

#print(table_record_ids)

# Delete all records in table
for record in table_record_ids:
    response = requests.delete(base_table_api_url + '/' + record, headers=headers)
    #print(response)
# Is possible to delete 10 at a time if wanting to limit # of requests for any reason


# Take Data from source and upload to Airtable

df = pd.read_excel('AirTableData.xlsx')
result = df.to_json(orient="records")
parsed = json.loads(result)
#json_data = json.dumps(parsed, indent=4)
#print(parsed)

for i in parsed:
    temp_json = {'fields' : i}
    records = [temp_json]
    data = {'records' : records}
    response = requests.post(base_table_api_url, headers=headers, json=data)
    print(response.content)


