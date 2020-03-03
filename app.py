from pymongo import MongoClient
from pprint import pprint
from bson.json_util import loads
import json
import datetime


client = MongoClient()
db = client.nasa
meteorites = db.meteorites


def findName(name):
        for meteorite in meteorites.find({"name" : str(name)}):
                print(meteorite)


def findMass(mass):
        for meteorite in meteorites.find({"mass": str(mass)}):
                print(meteorite)


def findYear(year):
        for meteorite in meteorites.find():
            print(meteorite)
            yeartemp = meteorite["year"][:4]
            if (yeartemp == year):
                print(yeartemp)


def findCoordinates(lat, long):
        for meteorite in meteorites.find({"reclat" :str(lat), "reclong": str(long)}):
                print(meteorite["reclat"] + ", " + meteorite["long"])


# findName("Aachen")
# findMass(21)
findYear(1957)
#findByZip(11234)
#findByBorough("Bronx")
#findByZipWithScoreCap(10280, 8)
#findByZipAndGrade(10280, "C")
