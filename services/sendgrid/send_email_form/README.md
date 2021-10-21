# Sendgrid Form to Email Tool
This is for creating a service to allow users to send sendgrid emails via api or web form. 

## How it works:
This tool allows an administrator to have one Sendgrid "master" api token.
They can then distribute self made keys to team members who they would like to be able to use their master api token without giving the master token to them.
These distributed keys can be used in a web form or via url to send an email.

There are two options to send emails with this tool
<ul>
<li>Send via post request with json payload</li>
<li>Use a hosted form to submit the information ( generates the payload to send + Post request )</li>
</ul>

## Requirements:
A Sendgrid account / API Token

## Setup:
### Create a Lair 
Lairs are preconfigured environments hosted by WayScript. To create a Lair, signin to wayscript and click " + New Lair."

### Upload files:
Download from GitHub and upload to WSX the files within send_email_form
Your file directory inside your lair should look like this:
<p align="center">
  <img width="300" src="https://raw.githubusercontent.com/wayscript/wsx_tools/master/static/sendgrid/sendgrid_send_email_form_directory.jpg" />
</p>

### Setup Secrets
<p align="center">
  <img src="https://raw.githubusercontent.com/wayscript/wsx_tools/master/static/sendgrid/sendgrid_secrets_send_email.jpg" />
</p>

You will need to place your sendgrid provided api token into your wayscript .secrets file.
The name of this token should be ```sendgrid_api_token```

### Configure App.py
Inside of App.py create arbitrary keys that you will give access to using your tool.
These are up to you and are intended to be given to those who you want to access your tool ( without giving your sendgrid api token away.)
The names of these tokens should be placed in accepted_tokens in app.py file ( line 12 )

Fill in the from email address variable, this will be the email addresss you used to sign up with sendgrid.

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

### Testing your tool
You can test your tool by visiting the url provided in your deploy trigger, or sending a request to the url.

A sample request may look like:
```Python
import requests

data = {'to_email':'derrick@wayscript.com',
'subject':'Greetings!',
'content_to_send':'hello!',
'api_token': 'derrick_token'}

url = 'https://5362804a-e9e6-4c90-ae1c-9a76e5fc4df7.wayscript.cloud/send_email'

response = requests.post(url, json = data)
print(response.content)
```
