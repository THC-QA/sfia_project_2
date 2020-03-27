from flask import Flask, request
from requests import post, get
from json import dumps
from random import choice

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    speed_modifiers = ["snap", "lightning", "quick", "flying", "speed"]
    heavy_modifiers = ["cleaving", "explosive", "impact", "destructive", "heavy"]
    perk = request.cookies.get("perk") # get("http://localhost:5000/") # request.json
    print(perk)
    if perk["perk"] == "speed":
        modifier = {"modifier" : choice(speed_modifiers)}
    else:
        modifier = {"modifier" : choice(heavy_modifiers)}
    # post("http://localhost:5003/", json=modifier)
    return modifier