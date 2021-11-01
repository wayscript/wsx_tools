# my-lair-a > app.py

from flask import Flask, render_template, request
from tinydb import TinyDB, Query

app = Flask(__name__)

@app.route('/get_data', methods = ['GET'])
def get_data():
    query_param_value = request.args.get('value')
    db = TinyDB('db.json')
    Entry = Query()
    search = db.search(Entry.value == query_param_value)
    return {"Result": str(search)

@app.route('/submit_entry', methods = ['GET', 'POST'])
def submit_entry():
    if request.method == 'POST':
        value        = request.json.get('value')
        amount        = request.json.get('amount')
        db = TinyDB('db.json')
        db.insert({'value': value, 'amount': float(amount)})
        return {"message": "Success"}
    else:
        return 'Please Send POST for submitting data'

if __name__ == '__main__':
    app.run()
