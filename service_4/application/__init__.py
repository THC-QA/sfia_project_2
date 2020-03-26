from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/string')
def requestFunction():
    return "Service 4 returns this String\n" 