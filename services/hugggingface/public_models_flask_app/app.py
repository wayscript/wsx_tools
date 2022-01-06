import os

from flask import Flask, request, render_template
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#built in pages
@app.route('/form')
def sentiment_form():
    return render_template('form.html')

@app.route('/sentiment_form')
def form():
    return render_template('sentiment_form.html')

#APIs
@app.route('/bert', methods = ['GET', 'POST'])
def bert():
    if request.json:
        string = request.json.get('string')
    if request.form:
        string = request.form.get('string')

    token = os.environ.get('huggingface_token')

    API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"inputs": str(string)}

    response = requests.post(API_URL, headers=headers, json=payload)

    top_response = response.json()[0]

    return top_response

@app.route('/sentiment', methods = ['GET', 'POST'])
def sentiment():
    if request.json:
        string = request.json.get('string')
    if request.form:
        string = request.form.get('string')

    token = os.environ.get('huggingface_token')

    API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"inputs": str(string)}

    response = requests.post(API_URL, headers=headers, json=payload).json()

    return {'response':response}

if __name__ == '__main__':
    app.run()
