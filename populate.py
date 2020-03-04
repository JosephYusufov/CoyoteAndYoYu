# Joseph "Yo-Yu" Yusufov, William "Coyote" Lin
# SoftDev pd 02
# K10: Import / Export Bank
# 2020-03-04

# See app.py for our description.

from pymongo import MongoClient
from pprint import pprint
from bson.json_util import loads
import json
import datetime

client = MongoClient()
db = client.WhoLetTheDogsOut
meteorites = db.meteorites
meteorites.delete_many({})

with open("meteorites.json", 'r') as file:
    data = json.load(file)
    for member in data:
        id = meteorites.insert_one(loads(json.dumps(member)))
        print(id)
