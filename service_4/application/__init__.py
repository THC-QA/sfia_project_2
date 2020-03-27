from flask import Flask, request
from requests import get
from json import dumps
from random import choice

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    titles = []
    character = request.cookies.get("character") # get("http://localhost:5000/")
    print(character)
    combat = get("http://localhost:5001/")
    print(combat)
    modifier = get("http://localhost:5002/") # request.json
    print(modifier)
    character.update(combat)
    character.update(modifier)
    # post("http://localhost:5000/browse", json = character)
    return combat