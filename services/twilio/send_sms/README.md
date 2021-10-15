# Twilio Send SMS Tool
This is for creating a service to allow users to send Twilio SMS Messages.

## How it works:
This tool allows an administrator to have one Twilio "master" api token.
They can then distribute self made keys to team members who they would like to be able to use their master api token without giving the master token to them.
These distributed keys can be used in a web form or via url to send a SMS message.

There are two options to send messages with this tool
<ul>
<li>Send via url + query parameters</li>
<li>Use a hosted form to submit the information ( generates the query parameter string )</li>
</ul>

## Requirements:
A Twilio account / API Token

## Setup:
### Create a Lair
Lairs are preconfigured environments hosted by WayScript. To create a Lair, signin to wayscript and click " + New Lair."

### Upload files:
Download from GitHub and upload to WSX the files within twilio/send_sms
Your file directory inside your lair should look like this:
