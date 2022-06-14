from app import app
from flask import render_template

@app.route('/')
def index():
    name = "Alicja Deja"
    return render_template("index.html.jinja", name=name)

@app.route('/author')
def author():
    return render_template("author.html.jinja")
