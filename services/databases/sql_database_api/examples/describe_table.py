import requests

payload = {"table":"users"}

response = requests.post('<WAYSCRIPT-TRIGGER-URL>/describe_table', json=payload)
print(response.content)
