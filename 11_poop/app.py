from flask import Flask, render_template, request
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

@app.route("/meteorites", methods=['GET', 'POST'])
def meteorites():
    select = request.form.get("meteorites")
    print(select)
    return render_template("meteorites.html")

@app.route("/nobel")
def nobel():
    return render_template("nobel.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
