from flask import Flask, request, url_for
from flask_mysqldb import MySQL
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
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

def multiselect_set_selections(driver, element_id, labels):
    el = driver.find_element_by_id(element_id)
    for option in el.find_elements_by_tag_name('option'):
        if option.text in labels:
            option.click()

def multiselect_set_selections_invert(driver, element_id, label):
    el = driver.find_element_by_id(element_id)
    for option in el.find_elements_by_tag_name('option'):
        if label in option.text:
            option.click()

def test_empty():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT concat('DROP TABLE IF EXISTS `', table_name, '`;') FROM information_schema.tables WHERE table_schema = 'testing';")
        drops = cur.fetchall()
        mysql.connection.commit()
        cur.execute("SET FOREIGN_KEY_CHECKS = 0")
        mysql.connection.commit()
        for drop in drops:
            cur.execute(drop[0])
            mysql.connection.commit()
        cur.execute("SET FOREIGN_KEY_CHECKS = 1")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        empty = len(cur.fetchall())+1
        mysql.connection.commit()
        cur.close()
        assert empty

def test_create_characters():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SHOW tables;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("CREATE TABLE characters(id INT(5) NOT NULL AUTO_INCREMENT, data VARCHAR(100), PRIMARY KEY(id));")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 1

def test_character_insert():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM characters;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/google-chrome"
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
        driver.get("https://127.0.0.1/")
        driver.find_element_by_name("name").send_keys("Test")
        multiselect_set_selections(driver, "type", "melee")
        multiselect_set_selections(driver, "perk", "heavy")
        driver.find_element_by_id("submit_new").click()
        sleep(3)
        cur.execute("SELECT * FROM characters;")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start-end) == 1
        assert url_for('/') in driver.current_url
        new_submission = driver.find_element_by_id("display_content").text
        driver.quit()
        assert "Test" in new_submission
        assert "melee" in new_submission
        assert "heavy" in new_submission

def test_character_update():
    with app.app_context():
        cur = mysql.connection.cursor()
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/google-chrome"
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
        driver.get("https://127.0.0.1/")
        multiselect_set_selections_invert(driver, "data", "Test")
        driver.find_element_by_id("new_data").send_keys("PLACEHOLDER")
        driver.find_element_by_id("submit_update").click()
        sleep(3)
        cur.execute("SELECT FROM characters WHERE data='PLACEHOLDER';")
        selection = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert selection
        assert url_for('/') in driver.current_url
        driver.quit()

def test_character_deletion():
    with app.app_context():
        cur = mysql.connection.cursor()
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/google-chrome"
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
        driver.get("https://127.0.0.1/")
        multiselect_set_selections(driver, "datad", "PLACEHOLDER")
        driver.find_element_by_id("submit_delete").click()
        sleep(3)
        cur.execute("SELECT * FROM characters;")
        present = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert not present
        assert url_for('/') in driver.current_url
        driver.quit()