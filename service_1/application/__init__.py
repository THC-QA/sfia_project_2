from flask import Flask, render_template, url_for, request
from requests import post, get
# from json import dumps
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRETKEY")
app.config['MYSQL_HOST'] = os.getenv('MYSQLHOST')
app.config['MYSQL_USER'] = os.getenv('MYSQLUSER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQLPASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQLDB')

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        details = request.form
        name = details["name"]
        combat = details["type"]
        perk = details["perk"]
        # character.update(combat)
        # character.update(perk)
        # character = dumps(character)
        # combat = dumps(combat)
        # perk = dumps(perk)
        print(name)
        print(combat)
        print(perk)
        # post("http://localhost:5001/", json=combat)
        # post("http://localhost:5002/", json=perk)
        # post("http://localhost:5000/send", json=character)
        content = get("http://localhost:5003/?name={0}&combat={1}&perk={2}".format(name,combat,perk)).text
        # print(request.cookies.get("name"))
        print(content)
        cur = mysql.connection.cursor()
        cur.execute("INSERT IGNORE INTO characters(data) VALUES (%s);", [content])
        mysql.connection.commit()
        cur.close()
        return render_template('home.html', content=content)
    # print(app.config["MYSQL_HOST"])
    # print(app.config["MYSQL_USER"])
    # print(app.config["MYSQL_DB"])
    # print(app.config["SECRET_KEY"])
    return render_template('home.html', content="Please Submit")

# def cookie(character):
#     # character = {"name":"test","type":"melee","perk":"heavy"}
#     char_ind = [key for key in character]
#     res = make_response("test_cookie")
#     for key in char_ind:
#         res.set_cookie(key, value=character[key])
#     # for key in char_ind:
#     #     print(request.cookies.get(key))
#     return res


# @app.route('/browse', methods=['GET'])
# def browse():
#         # response = request.json
#         response = get("http://localhost:5003/")
#         print(response)
#         return response # render_template('browse.html', sentence = sentence, title = 'Browse')

# @app.route('/send', methods=["GET"])
# def send():
#     character = request.json
#     print(character)
#     return character