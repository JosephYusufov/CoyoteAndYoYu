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
def meteoritesRoute():
    if request.args:        
        print(request.args["query"])
        print(request.args["field"])
        if request.args["field"] == "name":
            toDisplay = meteorites.findName(request.args["query"])
        elif request.args["field"] == "mass":
            tpDisplay = meteorites.findMass(request.args["query"])
        elif request.args["field"] == "year":
            toDisplay = meteorites.findYear(request.args["query"])
        elif request.args["field"] == "coordinates":
            toDisplay = meteorites.findCoordinates(request.args["query"])        
        return render_template("meteorites.html", data=toDisplay)
    return render_template("meteorites.html")


@app.route("/nobel")
def nobelRoute():
    toDisplay = None
    if request.args:
        print(request.args["query"])
        print(request.args["field"])
        if request.args["field"] == "topic":
            toDisplay = prize.findTopic(request.args["query"])
        if request.args["field"] == "year":
            toDisplay = prize.findTopic(str(request.args["query"]))
        #print(toDisplay)
        return render_template("nobel.html",data = toDisplay)
    return render_template("nobel.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
