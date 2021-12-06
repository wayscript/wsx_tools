import requests

payload = {"table":"users"}


response = requests.post('http://127.0.0.1:5000/get_all_from_table', json=payload)
print(response.content)
