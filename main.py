from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá mundo!'

@app.route('/gamelegal')
def gamelegal():
    return 'Legal'

@app.route('/legal/<nome>')
def legal(nome):
    nome = escape(nome)
    return f"<h1>Olá, {nome}<h1>"

if __name__ == '__main__':
    app.run(debug=True)