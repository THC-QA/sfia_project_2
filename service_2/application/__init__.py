from flask import Flask, request
from requests import post, get
from json import dumps
from random import choice

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    melee_skills = ["bash", "slash", "pierce", "sweep", "scrape", "tap", "block", "parry", "dual weilding", "riposte"]
    ranged_skills = ["power shot", "spin", "curve", "multi-shot", "ricochet", "quick shot", "precise shot", "collision", "scatter shot", "point-blank shot"]
    combat = request.cookies.get("type") # get("http://localhost:5000/") # request.json
    print(combat)
    if combat["type"] == "melee":
        skill = {"skill" : choice(melee_skills)}
    else:
        skill = {"skill" : choice(ranged_skills)}
    # post("http://localhost:5003/", json=skill)
    return skill