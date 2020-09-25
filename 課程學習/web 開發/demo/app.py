from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/header')
def header():
    return render_template("header.html")