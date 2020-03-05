from flask import Flask, render_template
from meteorites import meteorites
from nobel import mongo
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

mongo.printHi()
meteorites.printHi()

@app.route("/")
def something():
    render_template("login.html")

if __name__ == "__main__":
    app.debug = True()
    app.run()
