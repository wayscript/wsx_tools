import requests

payload = {"table":"users", "value":'(1000, "Mike", 99)'}

response = requests.post('https://secluded-canary-basement.wayscript.cloud/create_entry', json=payload)
print(response)
