from flask import Flask, render_template
from meteorites import meteorites
from nobel import prize
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

prize.printHi()
meteorites.printHi()

@app.route("/")
def welcome():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
