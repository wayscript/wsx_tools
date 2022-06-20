from wayscript import context
from wayscript.triggers import http_trigger
import json

# Get payload for request event
request_payload = context.get_event()
print(request_payload)

# Specify response payload
response_payload = {"hello": 'world'}
response_headers = {"content-type": "application/json"}
status_code = 200

request_body = json.loads(request_payload['data'].get('data'))

if request_body.get('somekey') == 'somevalue':
    response_payload = {"response": "action performed"}

# Send response
http_trigger.send_response(data=response_payload, headers=response_headers, status_code=status_code)
