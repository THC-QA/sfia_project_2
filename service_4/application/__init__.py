from flask import Flask, request
from requests import get
# from json import dumps
from random import choice

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    titles = ["the Brave", "the Bold", "the Beautiful", "of Ill Repute", "Drunkard and Wastrel", "Inveterate Flirt", "the Terrible", "the Destroyer", "'Blackheart'", "Slayer of {0}".format(choice(enemies))]
    enemies = ["Kings", "Dragons", "Demons", "Maidens", "Trolls", "Goblins", "Unicorns", "Beastmen", "Vampires", "the Undead", "Taxmen", "the Poor", "Passing Innocents"]
    # character = request.cookies.get("character") # get("http://localhost:5000/")
    name = request.args.get("name")
    print(name)
    if 'test' not in name:
        name = name + ", " + choice(titles)
    perk = request.args.get("perk")
    print(perk)
    combat = request.args.get("combat")
    print(combat)
    modifier = get("http://localhost:5002/?perk={0}".format(perk)).text # request.json
    print(modifier)
    skill = get("http://localhost:5001/?combat={0}".format(combat)).text
    print(skill)
    character={"Name":name,"Role":" ".join([perk,combat]),"Signature Skill":" ".join([modifier,skill])}
    # character.update(combat)
    # character.update(modifier)
    # post("http://localhost:5000/browse", json = character)
    return character