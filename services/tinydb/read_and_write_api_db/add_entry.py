from tinydb import TinyDB, Query

db = TinyDB('db.json')
db.insert({'value': 'Product A', 'amount': 50.0})
