from pymongo import MongoClient
from pprint import pprint
from bson.json_util import loads
import json
import datetime


client = MongoClient()
db = client.test
restaurants = db.restaurants


def findByZip(zip): 
        for restaurant in restaurants.find({"address.zipcode" : str(zip)}):
                print(restaurant["name"])        

    
def findByBorough(borough):
        for restaurant in restaurants.find({"borough": borough}):
                print(restaurant["name"])


def findByZipWithScoreCap(zip, score):
        for restaurant in restaurants.find({"address.zipcode" : str(zip), "grades.score": {"$lt": score}}):
                print(restaurant["name"])


def findByZipAndGrade(zip, grade):
        for restaurant in restaurants.find({"address.zipcode" :str(zip), "grades.grade": grade}):
                print(restaurant["name"])

                      
#findByZip(11234)
#findByBorough("Bronx")
#findByZipWithScoreCap(10280, 8)
#findByZipAndGrade(10280, "C")
