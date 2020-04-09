from flask import Flask, request
from flask_mysqldb import MySQL
from selenium import webdriver
import os

app = Flask(__name__)

# Call config variables from pre-assigned environmentals, check Jenkinsfile for preferred source

app.config['SECRET_KEY'] = os.environ['SECRETKEY']
app.config['MYSQL_HOST'] = os.environ['MYSQLHOST']
app.config['MYSQL_USER'] = os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB'] = os.environ['MYSQLDB']

mysql = MySQL(app)

# Start stable test loop

driver = webdriver.Chrome()
driver.get("https://localhost/")

if foo do x: