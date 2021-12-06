import requests

payload = {"table":"users", "value":"(2, 'Mike', 24)"}

response = requests.post('http://127.0.0.1:5000/create_entry', json=payload)
print(response.content)
