# Below are all the routes to interact with your database via API

import os

from flask import Flask, render_template, request

# App Logic
app = Flask(__name__)

## FETCHING DATA FROM DATABASE TABLE
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()