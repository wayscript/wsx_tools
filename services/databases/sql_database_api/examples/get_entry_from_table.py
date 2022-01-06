import requests

payload = {"table":"users", "column":"id", "value":"1000"}

response = requests.post('https://secluded-canary-basement.wayscript.cloud/get_entry_from_table', json=payload)
print(response.content)
