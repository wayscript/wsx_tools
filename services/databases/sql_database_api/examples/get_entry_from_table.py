import requests

payload = {"table":"users", "column":"id", "value":"2"}

response = requests.post('<WAYSCRIPT-TRIGGER-URL>/get_entry_from_table', json=payload)
print(response.content)
