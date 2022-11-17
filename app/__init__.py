from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


@app.rout("/contatos")
def contatos():
    return "Lista de Contatos"