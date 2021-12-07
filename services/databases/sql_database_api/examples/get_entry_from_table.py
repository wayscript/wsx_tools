import requests

payload = {"table":"users", "column":"id", "value":"2"}

response = requests.post('http://127.0.0.1:5000/get_entry_from_table', json=payload)
print(response.content)
