import requests

payload = {"table":"users"}

response = requests.post('http://127.0.0.1:5000/describe_table', json=payload)
print(response.content)
