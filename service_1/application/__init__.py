from flask import Flask, render_template, redirect, url_for, request, make_response
from requests import post, get
from json import dumps

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        details = request.form
        character = {"name" : details["name"]}
        combat = {"type" : details["type"]}
        perk = {"perk" : details["perk"]}
        character.update(combat)
        character.update(perk)
        # character = dumps(character)
        # combat = dumps(combat)
        # perk = dumps(perk)
        print(character)
        print(combat)
        print(perk)
        # post("http://localhost:5001/", json=combat)
        # post("http://localhost:5002/", json=perk)
        # post("http://localhost:5000/send", json=character)
        cookie(character)
        print(request.cookies.get("name"))
        return redirect(url_for("browse"))
    return render_template('home.html', title="home")

def cookie(character):
    # character = {"name":"test","type":"melee","perk":"heavy"}
    char_ind = [key for key in character]
    res = make_response("test_cookie")
    for key in char_ind:
        res.set_cookie(key, value=character[key])
    # for key in char_ind:
    #     print(request.cookies.get(key))
    return res


@app.route('/browse', methods=['GET'])
def browse():
        # response = request.json
        response = get("http://localhost:5003/")
        print(response)
        return response # render_template('browse.html', sentence = sentence, title = 'Browse')

# @app.route('/send', methods=["GET"])
# def send():
#     character = request.json
#     print(character)
#     return character