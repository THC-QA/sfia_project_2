from flask import Flask, request
from random import choice

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    speed_modifiers = ["snap", "lightning", "quick", "flying", "speedy"]
    heavy_modifiers = ["cleaving", "explosive", "impact", "destructive", "heavy"]
    perk = request.args.get("perk")
    print(perk)
    if perk == "speed":
        modifier = choice(speed_modifiers)
    else:
        modifier = choice(heavy_modifiers)
    return modifier