from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        details = request.form
        name = details["name"]
        combat = details["type"]
        perk = details["perk"]
        return redirect(url_for("/browse")
    return render_template('home.html')

@app.route('/browse', methods=['GET'])
def browse():
        response = requests.get('http://service4:5000/title')
        print(response)
        sentence = response.text
        return render_template('browse.html', sentence = sentence, title = 'Browse')