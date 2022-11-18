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

@app.route('/submit-meeting', methods=['GET', 'POST'])
def submit_meeting():
    name = request.form.get('name')
    email = request.form.get('email')
    details = request.form.get('details')
    ### Do something with the data here
    print(name)
    return render_template('home.html')

@app.route('/payments')
def payments():
    return render_template('payments.html')

if __name__ == '__main__':
    app.run()
