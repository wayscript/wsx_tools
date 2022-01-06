import requests

WAYSCRIPT_BASE_URL = ''
url = WAYSCRIPT_BASE_URL + '/sentiment'

payload = {"string": 'this is the string to change'}

response = requests.post(url, json=payload)
