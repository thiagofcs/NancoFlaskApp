from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Nanco Corporation 2022(C)"