import requests
from wayscript import context

payload = {
    "bucket":"Bucket-Name",
    "key":"KeyToObject"
}

headers = {
    'Authorization': 'Bearer  d15a5b0e-c0a1-42fe-a73c-e8e2dbacdc3d'
}
lair_endpoint_url = 'https://surprisingly-spry-kudzu-clubhouse-dev.wayscript.cloud/get-object'

response = requests.post(lair_endpoint_url, json=lair, headers=headers)
print(response.content)