import requests

payload = {"table":"users", "value":'(6, "Mike", 99)'}

response = requests.post('<WAYSCRIPT-TRIGGER-URL>/create_entry', json=payload)
print(response.content)
