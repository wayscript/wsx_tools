# TinyDB Simple Read/Write Database via API
This is code to stand up a simple API which allows users to read and write information from a TinyDB database via WayScript X. 

## How it works:

## Requirements:

## Setup:
### Create a Lair 
Lairs are preconfigured environments hosted by WayScript. To create a Lair, signin to wayscript and click " + New Lair."

### Upload files:
Download from GitHub and upload to WSX the files within read_and_write_api_db

### Host your Tool
Host your tool by creating a deploy trigger within your .triggers file

The command to run will be:
```Python
flask run --port 8080 --host 0.0.0.0
```
Port ```8080```
For additional help on running servers please see:
https://wsxdocs.wayscript.com/quickstart/host-a-flask-server

This will host your tool at the provided url in the trigger

A nice to have, if you want to make changes and have them immediately reflect in your flask application is to set an environment variable
```Python
FLASK_ENV = development
```
This enables hot reloading as you make changes to your files.

### Testing your tool
You can test your tool by visiting the url provided in your deploy trigger, or sending a request to the url.

A sample request may look like:
```Python
import requests

params = {'value':'Product A'}

url = '<WAYSCRIPT-DEPLOY-TRIGGER-URL>/get_data'

response = requests.get(url, params = params)
print(response.content)
```
