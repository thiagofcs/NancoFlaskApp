from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def homepage():
    user = {'username': 'Thiago FCS'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    
    return render_template("index.html", title='Home', user=user, posts=posts)   


@app.route("/contatos")
def contatos():
    return "Lista de Contatos"