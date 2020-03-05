# Joseph "Yo-Yu" Yusufov, William "Coyote" Lin
# SoftDev pd 02
# K10: Import / Export Bank
# 2020-03-04

# Dataset: Earth Meteorite Landings
# Description: A collection of basic information about 1000 meteorites that have landed on the earth
#     since the 1800s
# Link: https://data.nasa.gov/resource/y77d-th95.json
# Summary: We used a separate script (populate.py) to import the json file into the Mongo database. For
#     most functions in this script, we use the db.collection.find() method, with the parameters that we
#     are searching for to retrieve the data we want. In one case, for the findYear() function, we had to
#     use a try except structure, because one of the meteorites did not have a year reported.

from pymongo import MongoClient
from pprint import pprint
from bson.json_util import loads
import json
import datetime


client = MongoClient()
db = client.WhoLetTheDogsOut
meteorites = db.meteorites


def findName(name):
        for meteorite in meteorites.find({"name" : str(name)}):
                pprint(meteorite)


def findMass(mass):
        for meteorite in meteorites.find({"mass": str(mass)}):
                pprint(meteorite)


def findYear(year):
        i = 0
        for meteorite in meteorites.find():
                try:
                        yeartemp = meteorite["year"][:4]
                        if (yeartemp == str(year)):
                                pprint(meteorite)
                except: pass


def findCoordinates(lat, long):
        for meteorite in meteorites.find({"$and":[
                        {"reclat" : { "$gt": str(lat-2), "$lt": str(lat+2)}},
                        {"reclong" : { "$gt": str(long-2), "$lt": str(long+2)}}
                        ]}):
                pprint(meteorite)

def printHi():
    print("Hello, meteorites")

print("=== FINDING NAME ===")
findName("Aachen")
print("=== FINDING MASS ===")
findMass(21)
print("=== FINDING YEAR ===")
findYear(1952)
print("=== FINDING COORDS (25, 105) ===")
findCoordinates(25, 105)
