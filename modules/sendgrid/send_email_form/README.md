# Sendgrid Form to Email Tool

## How it works:
This tool allows an administrator to have one Sendgrid "master" api token.
They can then distribute self made keys to team members who they would like to be able to use their master api token without giving the master token to them.
These distributed keys can be used in a web form or via url to send an email.

There are two options to send emails with this tool
1 - Send via url + query parameters
2 - Use a hosted form to submit the information ( generates the query parameter string )

## Setup:
### Upload files:
Download from GitHub and upload to WSX the files within send_email_form
Your file directory inside your lair should look like this:
![Directory](https://raw.githubusercontent.com/wayscript/wsx_tools/master/static/sendgrid/sendgrid_send_email_form_directory.jpg)

### Setup Secrets
Create arbitrary keys and values that you will give access to using your tool.
These are up to you and are intended to be given to those who you want to access your tool ( without giving your sendgrid api token away.)
The names of these tokens should be placed in accepted_tokens in app.py file ( line 14 )

You will need to place your sendgrid provided api token into your wayscript .secrets file.
The name of this token will be placed in your app.py file ( line 16 )

### Host your Tool
Host your tool by creating a deploy trigger within your .triggers file

The command to run will be:
```
flask run --port 8080 --host 0.0.0.0
```
For additional help on running servers please see:
https://wsxdocs.wayscript.com/quickstart/host-a-flask-server

This will host your tool at the provided url in the trigger
