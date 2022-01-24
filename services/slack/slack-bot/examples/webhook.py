import requests

headers = {
    'Content-type': 'application/json',
}

data = '{"text":"Hello, World!"}'

response = requests.post('https://hooks.slack.com/services/...', headers=headers, data=data)
print(response.content)
