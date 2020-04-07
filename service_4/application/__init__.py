from flask import Flask, request
from requests import get
from random import choice

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    enemies = ["Kings", "Dragons", "Demons", "Maidens", "Trolls", "Goblins", "Unicorns", "Beastmen", "Vampires", "the Undead", "Taxmen", "the Poor", "Passing Innocents"]
    titles = ["the Brave", "the Bold", "the Beautiful", "of Ill Repute", "Drunkard and Wastrel", "Inveterate Flirt", "the Terrible", "the Destroyer", "'Blackheart'", "Slayer of {0}".format(choice(enemies))]
    name = request.args.get("name")
    print(name)
    if 'test' not in name:
        if name == "Dave":
            name = name + ", " + titles[-1]
        name = name + ", " + choice(titles)
    perk = request.args.get("perk")
    print(perk)
    combat = request.args.get("combat")
    print(combat)
    modifier = get("http://modifier:5002/?perk={0}".format(perk)).text
    print(modifier)
    skill = get("http://skill:5001/?combat={0}".format(combat)).text
    print(skill)
    character={"Name":name,"Role":" ".join([perk,combat]),"Signature Skill":" ".join([modifier,skill])}
    return character