from flask import Flask, request
import boto3

from wayscript import context

import os 

app = Flask(__name__)

# AWS SETTINGS
# The secret key and access key come from an IAM user
# These secrets should be placed inside the .secrets file and then accessed using os
# For help creating an IAM user with permissions view the AWS docs
# https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html

region = 'us-east'
ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

# WayScript specific functions
# WayScript provides detailed information about the user when they access wayscript hosted endpoints
# This is done using the WayScript SDK
# For more information view:
# https://docs.wayscript.com/building-tools/sdk

def get_user_details():
  application_key = request.headers.get('Authorization')[7:]
  user = context.get_user_by_application_key(application_key)
  return user

# AWS Resource Calls
# Boto3 is used in this example to access AWS resources
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

def create_s3_client():
    client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
    )
    return client


@app.route('/create-bucket', methods=['GET', 'POST'])
def create_aws_resource_s3_bucket():
  if request.method != 'POST':
    return {'error': 'endpoint expected POST request with payload "project"'}
  if not request.json:
    return {'error': 'Missing Lair Context'}
  try:
    user = get_user_details()
  except:
    return {'data': 'logged out user.'}
  
  # Name Bucket
  # Name-Project-Env
  env_type = request.json.get('environment')
  project_name = request.json.get('name')
  
  bucket_name = str(user.get('first_name')) + "-" + project_name + "-" + env_type
  client = create_s3_client()
  response = client.create_bucket(Bucket=bucket_name.lower())
  return response 
  

if __name__ == '__main__':
  app.run()