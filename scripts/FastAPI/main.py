from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name : str
    description : Union[str, None] = None
    price : float
    tax : Union[str, None] = None

app = FastAPI()

@app.get("/")
def home():
    return {'data': 'Hello world'}

@app.get("/search/{item}")
def search(item: str):
    return {'data' : item}

@app.post("/items/")
def create_item(item : Item):
    return item
