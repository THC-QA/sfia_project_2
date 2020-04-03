from flask import Flask, request
from random import choice

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    melee_skills = ["bash", "slash", "pierce", "sweep", "scrape", "tap", "block", "parry", "dual weilding", "riposte"]
    ranged_skills = ["power shot", "spin", "curve", "multi-shot", "ricochet", "quick shot", "precise shot", "collision", "scatter shot", "point-blank shot"]
    combat = request.args.get("combat")
    print(combat)
    if combat == "melee":
        skill = choice(melee_skills)
    else:
        skill = choice(ranged_skills)
    return skill