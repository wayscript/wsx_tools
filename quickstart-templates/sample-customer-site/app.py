# Below are all the routes to interact with your database via API

import os

from flask import Flask, render_template, request

# App Logic
app = Flask(__name__)

## FETCHING DATA FROM DATABASE TABLE
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book-meeting')
def meeting():
    return render_template('meeting.html')

@app.route('/payments')
def payments():
    return render_template('payments.html')

if __name__ == '__main__':
    app.run()