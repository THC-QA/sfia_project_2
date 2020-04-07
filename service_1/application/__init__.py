from flask import Flask, render_template, url_for, request
from requests import post, get
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
        content = "Please Submit"
        if "name" in details:
            name = details["name"]
            combat = details["type"]
            perk = details["perk"]
            content = get("http://title:5003/?name={0}&combat={1}&perk={2}".format(name,combat,perk)).text
            cur = mysql.connection.cursor()
            cur.execute("INSERT IGNORE INTO characters(data) VALUES (%s);", [content])
        elif "new_data" in details:
            data = details["data"]
            new_data = details["new_data"]
            cur = mysql.connection.cursor()
            cur.execute('UPDATE characters SET data = "{0}" WHERE id = {1};'.format(new_data,data))
        else:
            data = details["data"]
            cur = mysql.connection.cursor()
            cur.execute('DELETE IGNORE FROM characters WHERE id = {};'.format(data))
        mysql.connection.commit()
        cur.execute("SELECT * FROM characters;")
        characters = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return render_template('home.html', content=content, characters=characters)
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM characters;")
    characters = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('home.html', content="Please Submit", characters=characters)