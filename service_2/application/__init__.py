from flask import Flask, request
import requests
from random import choice

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    melee_skills = []
    ranged_skills = []
    combat = requests.
    if combat == "melee":
        skill = melee_skills.choice()
        return skill
    else:
        skill = ranged_skills.choice()
        return skill