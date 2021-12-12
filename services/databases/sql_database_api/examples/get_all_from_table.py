import requests

payload = {"table":"users"}


response = requests.post('<WAYSCRIPT-TRIGGER-URL>/get_all_from_table', json=payload)
print(response.content)
