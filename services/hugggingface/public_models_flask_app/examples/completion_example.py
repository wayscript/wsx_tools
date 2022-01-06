import requests

WAYSCRIPT_BASE_URL = ''
url = WAYSCRIPT_BASE_URL + '/bert'

payload = {"string": 'The world is [MASK].'}

response = requests.post(url, json=payload)
