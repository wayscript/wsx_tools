from flask import Flask, request
from wayscript import context

app = Flask(__name__)

def get_user_details():
  # Parse application key from bearer token in request header
  application_key = request.headers.get('Authorization')[7:]
  # Query user object from application key
  user = context.get_user_by_application_key(application_key)
  return user

@app.route('/')
def hello_world():
  try:
    user = get_user_details()
  except:
    return {'data': 'logged out user.'}
  if user.get('email') != 'derrick@wayscript.com': #admin email
    return {'data':'data for consumer of api'}
  else:
    return {'data': 'data for system owner'}

if __name__ == '__main__':
  app.run()
