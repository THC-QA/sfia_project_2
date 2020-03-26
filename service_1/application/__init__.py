from flask import Flask, render_template, redirect, url_for, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        details = request.form
        character = details["name"]
        combat = details["type"]
        perk = details["perk"]
        # character.update(combat)
        # character.update(perk)
        character = json.dumps(character)
        combat = json.dumps(combat)
        perk = json.dumps(perk)
        print(character)
        print(combat)
        print(perk)
        requests.post("http://localhost:5001/", json=combat)
        requests.post("http://localhost:5002/", json=perk)
        requests.post("http://localhost:5003/", json=character)
        return redirect(url_for("browse"))
    return render_template('home.html', title="home")

@app.route('/browse', methods=['GET'])
def browse():
        response = requests.get('http://localhost:5003/')
        print(response)
        sentence = response.text
        print(sentence)
        return sentence # render_template('browse.html', sentence = sentence, title = 'Browse')