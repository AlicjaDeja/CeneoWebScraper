from app import app
from flask import render_template

@app.route('/')
def index():
    name = "Alicja Deja"
    return render_template("index.html.jinja", name=name)

@app.route('/author')
def author():
    return render_template("author.html.jinja")

@app.route('/extract')
def extraxt():
    return render_template("extract.html.jinja")

@app.route('/products')
def products():
    return render_template("products.html.jinja")

@app.route('/product/<product_id>')
def product(product_id):
    return render_template("product.html.jinja")

@app.route('/opinions')
def opinions():
    return render_template("opinions.html.jinja")