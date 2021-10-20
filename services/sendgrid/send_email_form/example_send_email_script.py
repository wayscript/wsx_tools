import requests

data = {'to_email':'derrick@wayscript.com',
'subject':'Greetings!',
'content_to_send':'hello!',
'api_token': 'derrick_token'}

url = 'https://5362804a-e9e6-4c90-ae1c-9a76e5fc4df7.wayscript.cloud/send_email'

response = requests.post(url, json = data)
print(response.content)
