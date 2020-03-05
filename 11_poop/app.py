from flask import Flask, render_template
import sqlite3
import os

#---
DB_FILE = "test.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND  name='userdata' ''')
if c.fetchone()[0] < 1:
    c.execute("CREATE TABLE userdata (username TEXT, password TEXT);")
#---

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def something():
    render_template("login.html")

if __name__ == "__main__":
    app.debug = True()
    app.run()
