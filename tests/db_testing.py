from flask import Flask, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Call config variables from pre-assigned environmentals, check Jenkinsfile for preferred source

app.config['SECRET_KEY'] = os.environ.get("SECRETKEY")
app.config['MYSQL_HOST'] = os.environ.get('MYSQLHOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('testing')

mysql = MySQL(app)

# Start stable test loop

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
        cur.execute("DROP TABLE IF EXISTS characters;")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("CREATE TABLE test_characters(id INT(5) NOT NULL AUTO_INCREMENT, data VARCHAR(100);")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 1

def test_characters_coherence():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DESCRIBE test_characters;")
        col = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert col == 2

def test_character_insert():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM test_characters;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("INSERT IGNORE INTO test_characters(data) VALUES 'TEST VALUE';")
        mysql.connection.commit()
        cur.execute("SELECT * FROM test_characters;")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 1

def test_character_update():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("UPDATE test_characters SET data='test_value' WHERE data='TEST VALUE';")
        mysql.connection.commit()
        cur.execute("SELECT * FROM test_characters WHERE data='test_value';")
        update = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert update

def test_character_deletion():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DELETE IGNORE FROM test_characters WHERE data = 'test_value';")
        mysql.connection.commit()
        cur.execute("SELECT * FROM test_characters;")
        deleted = len(cur.fetchall()) + 1
        mysql.connection.commit()
        cur.close()
        assert deleted