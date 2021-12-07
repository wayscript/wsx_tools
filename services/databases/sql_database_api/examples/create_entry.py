import requests

payload = { "table":"users",
            "values": '(100, "Steve", 34)'}

response = requests.post('http://127.0.0.1:5000/create_entry', json=payload)
print(response.content)
