import requests

headers = {
    'Authorization': 'Bearer pat1zGGcxgDBVmama.6d6249472f7ad775bfd5c3f3fb8ca6b5cae98d63f113689d8c69484e1d25a92b',
    'Content-Type': 'application/json',
}

json_data = {
    'description': 'A to-do list of places to visit',
    'fields': [
        {
            'description': 'Name of the apartment',
            'name': 'Name',
            'type': 'singleLineText',
        },
        {
            'name': 'Address',
            'type': 'singleLineText',
        },
    ],
    'name': 'Apartments',
}

response = requests.post('https://api.airtable.com/v0/meta/bases/appyWAikEbS3b7Ejy/tables', headers=headers, json=json_data)
print(response.content)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{\n    "description": "A to-do list of places to visit",\n    "fields": [\n      {\n        "description": "Name of the apartment",\n        "name": "Name",\n        "type": "singleLineText"\n      },\n      {\n        "name": "Address",\n        "type": "singleLineText"\n      },\n      {\n        "name": "Visited",\n        "options": {\n          "color": "greenBright",\n          "icon": "check"\n        },\n        "type": "checkbox"\n      }\n    ],\n    "name": "Apartments"\n  }'
#response = requests.post('https://api.airtable.com/v0/meta/bases/appyWAikEbS3b7Ejy/tables', headers=headers, data=data)