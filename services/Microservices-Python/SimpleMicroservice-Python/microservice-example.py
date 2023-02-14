from wayscript import context
from wayscript.triggers import http_trigger

import pandas as pd
import json

# Get payload for request event
request_payload = context.get_event()

# Parse header and request body from request payload
request_header = request_payload['data'].get('headers')
request_body = request_payload['data'].get('data')

# do something with data
data = json.loads(request_body)
df = pd.DataFrame(data)
df_described = df.describe()

# Specify response payload
response_payload = df_described.to_json()
response_headers = {"content-type": "application/json"}
status_code = 200

# Send response
http_trigger.send_response(data=response_payload, headers=response_headers, status_code=status_code)